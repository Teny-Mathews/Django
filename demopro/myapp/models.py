from django.db import models

class Student(models.Model):
    rollno=models.IntegerField()
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    place=models.CharField(max_length=20)
    marks=models.IntegerField()




