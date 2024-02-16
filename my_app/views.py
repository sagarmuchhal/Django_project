from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.shortcuts import HttpResponseRedirect
from django.http import HttpResponse
from django.template import loader
from .models import Contact_us,Gallery,Staff


def home(request):
    if request.method == 'GET':
        staffs = Staff.objects.all()
        return render(request,'index.html',
                {'view_staff':staffs})
    
def signin(request):
    # Your view logic here
    pass     

def profile(request):
    return render(request,'profile.html')



def about_url(request):
     if request.method == 'GET':
        staffs = Staff.objects.all()
        return render(request,'about.html',
                {'view_staff':staffs})
    

def client_contact(request):
    
    print(request.POST)
    if request.method=="POST":
        name=str(request.POST['name'])
        email=str(request.POST['email'])
        phone_number=str(request.POST['phone_number'])
        message=str(request.POST['message'])
        task = Contact_us(name=name,email=email,phone_number=phone_number,message=message)
        task.save()

    return render(request, 'contact.html')


def courses_url(request):
    return render(request,'courses.html')


def display_gellery(request):
 
    if request.method == 'GET':
        Gallerys = Gallery.objects.all()
        return render(request, 'display_gallery.html',
                    {'gallery_images': Gallerys})
    
    
def display_staff(request):
    if request.method == 'GET':
        staffs = Staff.objects.all()
        return render(request,'team.html',
                {'view_staff':staffs})