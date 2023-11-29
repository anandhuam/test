from django.db import models

# Create your models here.
class Department(models.Model):
    Name=models.CharField(max_length=255)
    def __str__(self)  :
        return self . name

class Teacher(models.Model):
    Name=models.CharField(max_length=255)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
       def __str__(self)  :
        return self . name

class Batch(models.Model):
    batch=models.CharField(max_length=255)
       def __str__(self)  :
        return self . batch


class Student(models.Model):
    Name=models.CharField(max_length=255)
    batch=models.ForeignKey(Department,on_delete=models.CASCADE)
    teacher=models.ForeignKey(Department,on_delete=models.CASCADE)

