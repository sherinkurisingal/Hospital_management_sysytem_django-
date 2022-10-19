

# Create your models here.
from random import choices
from django.db import models
DOCTOR_CHOICE=(
    ('General','General'),
    ('ENT','ENT'),
    ('Cardiology','Cardiology'),
    ('Gynochology','Gynocology'),
    ('Neurology','Neurology'),
    ('Pediatric','Pediatric'),
    ('Orthopedics','Orthopedics')
)



class Opdetails(models.Model):
    def __str__(self):
        return self.name  
    
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    gender=models.CharField(max_length=500)
    date=models.DateField()
    doctor_type=models.CharField(choices=DOCTOR_CHOICE,max_length=50)
    mobile=models.PositiveIntegerField()
