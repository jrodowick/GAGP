from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from .forms import *
from .models import *
from django.core import serializers
import json
# Create your views here.

def index(request):
    return render(request, 'index.html')

def locations(request):
    locations = Location.objects.all()
    return render(request, 'locations.html', {'locations':locations})

def events(request):
    if(request.method == 'POST'):
        form = EventForm(request.POST)
        if(form.is_valid()):
            mod_entry = Event(
                name = form.cleaned_data['event_name'],
                event_location = form.cleaned_data['event_location']
            )
            mod_entry.save()
    else:
        form = EventForm()
    return render(request, 'events.html', {'form':form})

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
