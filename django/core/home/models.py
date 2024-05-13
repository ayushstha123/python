from django.db import models

# Create your models here.

class Student(models.Model):
    id=models.AutoField()
    fullname=models.CharField(max_length=30)
    age=models.IntegerField(default=18)
    email=models.EmailField()
    address=models.TextField()
    image=models.ImageField()
    file=models.FileField()
    field=models.text