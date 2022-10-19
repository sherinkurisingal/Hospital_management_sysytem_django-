from django.shortcuts import render,redirect
from .forms import NewUserForm
from django.contrib.auth.models import User
# Create your views here.

def register(request):
    if request.method=='POST': 
      form=NewUserForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect("/stock/index")
    
    form= NewUserForm(request.POST)  
        
    context={
        'form':form,
     }
    return render(request,'users/register.html',context)