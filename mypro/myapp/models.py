from django.db import models

class Person(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    place=models.CharField(max_length=20)

class Movie(models.Model):
    name=models.CharField(max_length=20)
    director=models.CharField(max_length=20)
    year=models.IntegerField()