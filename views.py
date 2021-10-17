from django.http import HttpResponse
from .models import Farmer
from django.http import Http404
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout , authenticate
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.urls import reverse
from django.contrib import messages
import sys


# Create your views here.



def home(request):
    obj=Farmer.objects.all()
    context={
        "obj":obj,

    }
    return render (request, 'mkulima/home.html',context)


def index(request):
    obj=Farmer.objects.all()
    context={
        "obj":obj,

    }
    return render(request, 'mkulima/home.html',context)

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username=form.cleaned_data.get('username')
            messages.success(request, f"New Account Created: {username}")
            login(request, user)
            return redirect("mkulima:homepage")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")
    form = UserCreationForm
    return render(request, 'mkulima/register.html' , 
    context = {"form":form})   

def search(request):
    if request.method == "POST":
     searched = request.POST['searched']
     
     return render(request, 'mkulima/search.html',{'searched':searched, Farmer:Farmer})
    else:
     return render(request, 'mkulima/search.html', {})
        

    

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out succesfully")
    return redirect("/home")

def login_request(request):
    if request.method == "POST":
        form =  AuthenticationForm(request , data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username , password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are Logged in as {username}")
                return redirect("/home")
            else:
                messages.error(request , "Invalid username or password")
    else:
        messages.error(request , "Invalid username or password")


    form = AuthenticationForm()
    return render (request, "mkulima/login.html",{"form":form})

def news(request):
    return render(request, 'mkulima/news.html')

def contact(request):
    return render(request, 'mkulima/contact.html')

def about(request):
    return render(request, 'mkulima/about.html')

def services(request):
    return render(request, 'mkulima/services.html')

def kenyaseed(request):
    return render(request, 'mkulima/https://kenyaseed.com/')
