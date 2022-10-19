from django.urls import path
from doctor.views import list,med_assign
app_name='doctor'


urlpatterns = [
    path("list/",list,name='list'), 
    path("medassign/",med_assign,name='med_assigning')
] 
