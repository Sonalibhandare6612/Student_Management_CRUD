from django.db import models

# Create your models here.

class Student(models.Model):
    studentId = models.CharField(max_length=20,primary_key=True)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    regNumber = models.CharField(max_length=100)
    email = models.EmailField()
    course = models.CharField(max_length=50)
    
    
    
