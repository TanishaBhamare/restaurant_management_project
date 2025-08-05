from django.shortcuts import render,redirect
from .forms import ContactForm

def homepage(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'contact/home.html',{
                'form':ContactForm(),
                'success': True
            })
        else:
            form = ContactForm()
        return render(request, 'contact/home.html' ,{'form':form})        


