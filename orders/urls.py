from django.urls import path
from .views import *

urlpatterns = [
    path('api/menu/',get_menu,name='menu-api')
]