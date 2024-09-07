from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def home(request):
    # Checking if the user is loged in or not
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        #authentication
        user = authenticate(request , username=username , password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "u succesfully loged in :)")
            return redirect('home')
        else:
            messages.info(request, "there was an error and we cant log u in :(" )
            return redirect('home')
    else:
        return render(request , 'website/home.html')

def login_user(request): 
    pass

def logout_user(request):
    logout(request)
    messages.success(request, "u sussecfully loged out !!")
    return redirect('home')