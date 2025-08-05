from django.shortcuts import render
import requests

def homepage(request):
    try:
        response = request.get('http://localhost:8000/api/menu/')
        manu_items = response.json()
    except Exception as e:
        manu_items = []
    return render(request, 'restaurant/manu.html',{'menu_items':menu_items}) 

    #Creating template
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Restaurant Menu</title>
        <style>
        body{
            font-family: Arial,sans-serif;
            margin: 40px;
            background: #f8f8f8;
        }
        .menu {
            max-width: 800px;
            margin: auto;
        }
        .menu-item{
            background: white;
            padding: 20px;
            margin -bottopm: 15px;
            border-radius: 8px;
            box-shadow: 0 0 5px #ddd;
        }
        .menu-item h3 {
            margin-top:0;
        }
        .price{
            color:green;
            font-weight:bold;
        }
        </style>
    </head>
    <body>
        <div class="menu">
             <h1>Our Menu</h1>

                     <div class="menu-items">
                          <h3>{{ item.name}}</h3>
                          <p>{{item.description}}</p>
                          <p class="price">${{item.price}}</p>
                          </div>
                          <p>No menu items available at this time.</p>
        </div>
    </body>
    </html>        


