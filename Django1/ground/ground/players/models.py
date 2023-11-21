from django.db import models

# Create your models here.
class Department(models.Model):
    name=models.CharField(max_length=255)
    
class Batch(models.Model):
    batch=models.CharField(max_length=255)
    def __str__(self):
        return self.batch
class Students(models.Model):
    name=models.CharField(max_length=255)
    batch=models.ForeignKey(Batch,on_delete=models.CASCADE)
    