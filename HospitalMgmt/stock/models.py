from django.db import models

# Create your models here.
class Medicine(models.Model):
    def __str__(self):
        return self.med_name
    med_name=models.CharField(max_length=50)
    price=models.IntegerField()
    qty=models.IntegerField()
    desc=models.CharField(max_length=100)