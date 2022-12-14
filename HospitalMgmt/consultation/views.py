from django.shortcuts import render
from consultation.forms import Online_consultForm
from .models import Opdetails
from django.views import View

# Create your views here.
class ConsultView(View):
    def get(self,request):
        form=Online_consultForm()
        context={
            'form':form
        }
        return render(request,'consultation/online_consult.html',context)

    def post(self,request):
        form=Online_consultForm(request.POST)    
        if form.is_valid():
            form.save()
            return render(request,'consultation/online_consult.html',{'form':form})

def optkt(request,id):
   op=Opdetails.objects.get(id=id)
   context={
          'op':op
      }  
   return render(request,'consultation/optktgenerate.html',context)     