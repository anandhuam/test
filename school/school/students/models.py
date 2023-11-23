from django.db import models

# Create your models here.
class Department(models.Model):
    Name=models.CharField(max_length=255)

class Teacher(models.Model):
    Name=models.CharField(max_length=255)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)

class Batch(models.Model):
    batch=models.CharField(max_length=255)


class Student(models.Model):
    Name=models.CharField(max_length=255)
    batch=models.ForeignKey(Department,on_delete=models.CASCADE)
    teacher=models.ForeignKey(Department,on_delete=models.CASCADE)

