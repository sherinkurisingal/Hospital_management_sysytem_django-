from django.urls import path
from .views import add_patients,patientlist,add_bill,billgenerate
from . import views
app_name='patients'


urlpatterns = [
     path("",add_patients,name='add_patients'), 
     path("list/",patientlist.as_view(),name='list') ,
     path("add_bill/",add_bill,name='add_bill'),
     path("bill/",billgenerate.as_view(),name='billgenerate') ,

     
]