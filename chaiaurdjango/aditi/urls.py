
from django.urls import path

from . import views
 
#localhost: 8000/aditi
#localhost:8000/aditi/order
urlpatterns = [
   
    path('',views.all_chai , name='all_home'),
    path( 'order/', views.order, name='order'), 
   
]
