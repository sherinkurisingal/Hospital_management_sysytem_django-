from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Patient(models.Model):
    def __str__(self):
        return self.f_name
    user=models.OneToOneField(User,on_delete=models.CASCADE)    
    f_name=models.CharField(max_length=50)
    l_name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    place=models.CharField(max_length=50)
    age=models.IntegerField()
    gender=models.CharField(max_length=20)
    mob=models.PositiveIntegerField()
    email=models.EmailField()
    

class Bill(models.Model):
    patient_id=models.OneToOneField(Patient,on_delete=models.CASCADE)
    bill_no=models.IntegerField()
    bill_date=models.DateField() 
    bill_amt=models.IntegerField()
    