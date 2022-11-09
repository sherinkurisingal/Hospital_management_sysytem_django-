from django.shortcuts import render
import django_tables2 as tables
from django.contrib.auth.decorators import login_required
from .models import Patient,Bill
from django.shortcuts import render,redirect

# Create your views here.
@login_required 
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

def add_bill(request):
    if request.method=='POST':
         bill_no=request.POST.get('bill_no')
         bill_date=request.POST.get('bill_date')
         bill_amt=request.POST.get('bill_amt') 
         bill=Bill(bill_no=bill_no,bill_date=bill_date,bill_amt=bill_amt)
         bill.save()
         return redirect('/patients/billgenerate')
    return render(request,'patients/patientbill.html')   
             
class billgenerate(tables.SingleTableView):
    table_class = list
    queryset = Patient.objects.all()
    template_name = "billgenerate.html"