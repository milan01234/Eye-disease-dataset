from django.db import models

# Create your models here.
class Patient(models.Model):
    Patient_Name=models.CharField(max_length=50)
    Xender=models.CharField(max_length=50)
    Age=models.IntegerField()
    Eye_Image=models.FileField()
    Disease=models.CharField(max_length=50)
    