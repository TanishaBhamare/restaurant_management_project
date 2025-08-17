from django.shortcuts import render

def restaurant(request):
    return render(request,'restaurant.html')



from django.urls import path
from . import views

urlpatterns = [
    path('restaurant',views.restaurant_page,name='restaurant'),
    
]