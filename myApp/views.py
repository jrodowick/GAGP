from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from .forms import *
from .models import *

# Create your views here.

def index(request):
    return render(request, 'index.html')

def register(request):
    if(request.method == 'POST'):
        form = RegistrationForm(request.POST)
        if(form.is_valid()):
            user = form.save(commit = True)

            if(user is not None):
                login(request, user)
            return redirect('/')
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form':form})
