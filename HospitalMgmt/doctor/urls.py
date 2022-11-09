from django.urls import path
from doctor.views import list,med_assign,add_doctor
app_name='doctor'


urlpatterns = [
    path("list/",list,name='list'), 
    path("medassign/",med_assign,name='med_assigning'),
    path('add_doctor/',add_doctor,name='add_doctor'),
] 
