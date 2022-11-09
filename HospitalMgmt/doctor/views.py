from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from doctor.models import Doctor,Med_assign

# Create your views here.
def list(request):
    list=Doctor.objects.all()
    context={
        'list': list
    }
    return render(request,'doctor/doctor_list.html',context) 


@login_required
def add_doctor(request):
  if request.method=='POST':
    d_name=request.POST.get('d_name')
    specialisation=request.POST.get('specialisation')
    image=request.FILES['upload']
    d=Doctor(d_name=d_name,specialise=specialisation,image=image)
   
    d.save()
    return redirect('/doctor/list')
  return render(request,'doctor/add_doctor.html')   





def med_assign(request):
    if request.method=='POST':
         p_name=request.POST.get('p_name')
         d_name=request.POST.get('d_name')
         m_name=request.POST.get('m_name')
         desc=request.POST.get('desc') 
         
         med=Med_assign(p_name=p_name,d_name=d_name,m_name=m_name,desc=desc)
         med.save()
         return redirect('/doctor/med_assigning')
    return render(request,'doctor/medicineassign.html')

