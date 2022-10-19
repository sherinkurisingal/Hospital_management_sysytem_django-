from django.shortcuts import render
import django_tables2 as tables

from patients.models import Patient
from django.shortcuts import render,redirect

# Create your views here.
def add_patients(request):
    if request.method=='POST':
        f_name=request.POST.get('f_name')
        l_name=request.POST.get('l_name')
        adrs=request.POST.get('address')
        place=request.POST.get('place')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        mobile=request.POST.get('mobile')
        email=request.POST.get('email')  
        p=Patient(f_name=f_name,l_name=l_name,address=adrs,place=place,age=age,gender=gender,mob=mobile,email=email)
        p.save()
        return redirect('/patients/list')
    return render(request,'patients/add_patient.html')

# def patientlist(request):
#     p=Patient.objects.all() 
#     context={
#          'p':p
#      } 
#     return render(request,'patients/patient_list.html',context)     

class list(tables.Table):
   class Meta:
      model = Patient
 
class patientlist(tables.SingleTableView):
   table_class = list
   queryset = Patient.objects.all()
   template_name = "patient_list.html"
             
