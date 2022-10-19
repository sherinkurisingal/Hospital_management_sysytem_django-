
from django.urls import path
from consultation.views import ConsultView 
app_name='consultation'

urlpatterns = [
    path("consult/",ConsultView.as_view(),name='consult'),  
]