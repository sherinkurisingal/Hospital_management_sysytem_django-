from django.db import models
from django.contrib.auth.models import User
from patients.models import Patient

# Create your models here.
class Doctor(models.Model):
    def __str__(self):
        return self.med_name
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    d_name=models.CharField(max_length=50)
    specialise=models.CharField(max_length=50)    

class Med_assign(models.Model):
     def __str__(self):
         return self.P_name
     m_id=models.ForeignKey(Patient,on_delete=models.CASCADE,default=1)    
     P_name=models.CharField(max_length=50)
     d_name=models.CharField(max_length=50)
     m_name=models.CharField(max_length=50)    
     desc=models.CharField(max_length=100)