from django.shortcuts import render
from django.conf import settings
from .forms import ContactForm

def homepage(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            context = {
                'form':ContactForm(),
                'success': True,
                'restaurant_name':settings.Alpha
            }
            return render(request, 'contact/home.html',context) 
        else:
            context = {
                'form':form,
                'restaurant_name':settings.Alpha
                 }
                 return render(request,'contact/home.html',context)

        else:
            form = ContactForm()
            context = {
                'form': form,
                'restaurant_name':settings.Alpha
            }
            return render(request, 'contact/home.html',context) 



