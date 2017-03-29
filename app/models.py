from django.db import models

class Student(models.Model):
  full_name = models.CharField(max_length=50)

  def __str__(self):
    return full_name

class Course(models.Model):
  title =  models.CharField(max_length=50)

  def __str__(self):
    return title
