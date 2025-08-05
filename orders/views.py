from django.shortcuts import render
import requests

def homepage(request):
    try:
        response = request.get('http://localhost:8000/api/menu/')
        manu_items = response.json()
    except Exception as e:
        manu_items = []
    return render(request, 'restaurant/manu.html',{'menu_items':menu_items})        
