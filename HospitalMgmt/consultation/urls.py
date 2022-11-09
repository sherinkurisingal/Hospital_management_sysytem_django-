
from django.urls import path
from consultation.views import ConsultView
from .views import optkt 
app_name='consultation'

urlpatterns = [
    path("consult/",ConsultView.as_view(),name='consult'),  
    path("consult/",optkt,name='optkt')
]