from django.contrib import admin
from django.urls import path,include
from login import views
urlpatterns = [
    path('',views.login,name="login"),
    path('login',views.login,name="login"),
    path('register',views.register,name="register"),
    path('logout',views.logout,name="logout"),
    path('book',views.book,name="book"),
    path('logout',views.logout,name="logout")

]
