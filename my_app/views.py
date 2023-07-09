from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.shortcuts import HttpResponseRedirect
from django.http import HttpResponse
from django.template import loader
from .models import Contact_us


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
    return render(request,'index.html')

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
        print("11111111111111111111111111111111111", password[0])
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
    return render(request,'about.html')
    

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

# def showform(request):
#     # en=contact_u(name=request.POST.get('name'),cl=request.POST.get('class'),
#     #  mark=request.POST.get('mark'),gender=request.POST.get('gender'))
#     # en.save()
#     # str1="Data inserted to student table" 
#     # return render(request,'signup_student.html',{'msg':str1})
#     form= FormContactForm(request.POST or None)
#     if form.is_valid():
#         print(112237846)
#         form.save()
#     print(89670998)
#     context= {'form': form }
        
#     return render(request, 'contact.html', context)
