
from django.urls import path
from stock.views import samples,listing,detailing,deleting,adding,updating
app_name='stock'

urlpatterns = [
    path("samples/",samples,name='samples'),  
    path('list/',listing,name='listing'),
    path('list/add/',adding,name='adding'),
    path('list/update/<int:id>',updating,name='updating'), 
    path('list/<int:id>',detailing,name='detailing'), 
    path('list/delete/<int:id>',deleting,name='deleting'),
]