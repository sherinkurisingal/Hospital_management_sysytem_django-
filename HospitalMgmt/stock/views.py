# from typing_extensions import Required
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Medicine
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required

# Create your views here.


def listing(request):
     med=Medicine.objects.all() 
     context={
         'med':med
     } 
     return render(request,'stock/stocklist.html',context)     
                
@login_required 
def adding(request):
    if request.method=='POST':
         name=request.POST.get('name')
         price=request.POST.get('price')
         qty=request.POST.get('qty')
         desc=request.POST.get('desc') 
         
         med=Medicine(med_name=name,price=price,qty=qty,desc=desc)
         med.save()
         return redirect('/stock/listing')
    return render(request,'stock/add_stock.html')







def detailing(request,id):
      med=Medicine.objects.get(id=id)
      context={
          'med':med
      }  
      return render(request,'stock/stock_details.html',context)     



def deleting(request,id):
     med=Medicine.objects.get(id=id)   
     context={
         'med':med
              }  
     if request.method=='POST':   
        med.delete()
    
        return redirect('/stock/listing')
     return render(request,'stock/del_stock.html',context) 


   
def updating(request,id):
    med=Medicine.objects.get(id=id)
    if request.method=='POST':
         med.med_name=request.POST.get('name')
         med.price=request.POST.get('price')
         med.qty=request.POST.get('qty')
         med.desc=request.POST.get('desc') 
         med.save()
         return redirect('/stock/listing')
    
    context={
         'med':med
              }  
    return render(request,'stock/update_stock.html',context)  