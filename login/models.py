from django.db import models

class Book(models.Model):
     applicant = models.EmailField(max_length = 200,null=True)
     club = models.CharField(max_length=20)
     post = models.CharField(max_length=30)
     requirement=models.TextField()
     def __str__(self):
         return self.club
