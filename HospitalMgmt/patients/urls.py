from django.urls import path
from .views import add_patients,patientlist
from . import views
app_name='patients'


urlpatterns = [
     path("",add_patients,name='add_patients'), 
     path("list/",views.patientlist.as_view(),name='list') 
     
]