from django.shortcuts import render
from .models import Restaurant

def home(request):
    restaurant = Restaurant.objects.first()
    context = {
        "Alpha":restaurant.name if restaurant else "Alpha"
    }
return render(request,"home.html",context)