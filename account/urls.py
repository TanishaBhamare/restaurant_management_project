from django.shortcuts import render

def restaurant(request):
    return render(request,'restaurant.html')



from django.urls import path
from .views import *

urlpatterns = [
    path('',homepage,name='homepage'),
    
]