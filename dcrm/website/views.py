from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Record

# Create your views here.

def home(request):
    records = Record.objects.all()
    # Checking if the user is logged in or not
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password1")  # Adjust this to match your form field name
        # authentication
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You successfully logged in :)")
            return redirect('home')
        else:
            messages.info(request, "There was an error, and we can't log you in :(")
            return redirect('home')
    else:
        return render(request, 'website/home.html', {'records':records})
    

def login_user(request): 
    pass    

def logout_user(request):
    logout(request)
    messages.success(request, "u sussecfully loged out !!")
    return redirect('home')


def regester(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You successfully registered!")
                return redirect('home')
        else:
            messages.error(request, "There was an error with your registration. Please try again.")
    else:
        form = SignUpForm()

    return render(request, 'website/regester.html', {'form': form})