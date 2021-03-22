from django.shortcuts import HttpResponse ,render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login as dj_login,logout as dj_logout
from django.contrib.auth.decorators import login_required
from login.models import Book
# Create your views here.

@login_required(login_url='/login')
def book(request):
    messages.success(request,"You are successfully logged in")
    if request.method=="POST":
        applicant=request.user
        club=request.POST.get('club')
        post=request.POST.get('post')
        requirement=request.POST.get('requirement')
        book=Book(club=club,post=post,requirement=requirement,applicant=applicant)
        book.save()
        messages.success(request,"Requirement sent successfully,you will receive an email if a classroom is allocated")
    return render(request,'book1.html')
def login(request):
    if request.method=="POST":
        loginemail=request.POST['loginemail']
        loginpassword=request.POST['loginpassword']
        user=authenticate(username=loginemail,password=loginpassword)
        if user is not None:
            dj_login(request,user)
            return redirect('book')
        else:
            messages.error(request,"Please enter correct email and password")
            return redirect('login')
    return render(request,'login.html')
def register(request):
    if request.method=="POST":
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']
        if User.objects.filter(email=email).exists():
            messages.error(request,"Email already taken")
            return redirect('register')
        if (password == password2):
          user=User.objects.create_user(first_name=fname,last_name=lname,email=email,username=email,password=password)
          user.save()
          messages.success(request,"User registered successfully")
        else:
          messages.error(request,"Passwords did not match")
          return redirect('register')
    return render(request,'register.html')
def logout(request):
    dj_logout(request)
    return redirect('login')
