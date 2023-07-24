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


# Create your views here.
def signup(request):
    # if request.user.is_authenticated:
    #     return redirect('/')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username = username,password=password)
            login(request,user)
            # login(request, user, backend='django.contrib.auth.backends.ModelBackend')

            return redirect('/')
        else:
            return render(request, 'signup.html', {'form':form})
    else: 
        form = UserCreationForm()
        return render(request, 'signup.html', {'form':form})
    
def home(request):
    if request.method == 'GET':
        staffs = Staff.objects.all()
        return render(request,'index.html',
                {'view_staff':staffs})
    

def signin(request):
    if request.user.is_authenticated:
        return render(request,'home.html')
    if request.method == 'POST':
        username = request.POST['username']
        print(request.POST)
        print("11111111111111111111111111111111111")
        password = request.POST['password']
        print("11111111111111111111111111111111111")
        print(password)

        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/profile')
        else:
            msg = 'Error in login'
            form = AuthenticationForm(request.POST)
            return render(request,'login.html',{'form':form,'msg':msg})
    else: 
        form = AuthenticationForm()
        return render(request, 'login.html', {'form':form})
            
def profile(request):
    return render(request,'profile.html')


def signout(request):
    logout(request)
    return redirect('/')

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