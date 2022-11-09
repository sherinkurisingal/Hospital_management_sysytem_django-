from django.contrib import admin

from patients.models import Patient,Bill
from django.contrib import admin

# Register your models here.
admin.site.register(Patient)
admin.site.register(Bill)