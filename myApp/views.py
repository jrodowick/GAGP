from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login
from django.contrib.auth.models import User
from .forms import *
from .models import *
from django.core import serializers
import json

# Create your views here.

def index(request):
    if(request.method == 'GET'):
        selected = 'home'
        return render(request, 'index.html', {'selected':selected})

def about(request):
    if(request.method == 'GET'):
        selected = 'about'
        return render(request, 'about.html', {'selected':selected})

def profile(request):
    return render(request, 'profile.html')

def locations(request):
    if(request.method == 'GET'):
        locations = Location.objects.all()
        #
        # results = []
        # dict = {}
        #
        # for row in locations:
        #     dict = row.asDict()
        #     results.append(dict)
        # response = json.dumps(results)
        # print(results)
        return render(request, 'locations.html', {'locations':locations})

def local_event(request):
    if(request.method == 'POST'):
        locations = Location.objects.all()
        events = Event.objects.all()
        location_and_events = []
        location_results = []
        event_results = []
        dict = {}

        for row in locations:
            dict = row.asDict()
            location_results.append(dict)

        location_and_events.append(location_results)
        dict = {}

        for row in events:
            dict = row.asDict()
            dict['location'] = dict['location'].asDict()
            event_results.append(dict)

        location_and_events.append(event_results)
        #print(location_and_events[1])
        #location_and_events = location_results + event_results
        response = json.dumps(location_and_events, default = str)
        return HttpResponse(response, content_type = 'application/json')

def events(request):
    if(request.method == 'POST'):
        form = EventForm(request.POST)
        if(form.is_valid()):
            # mod_entry = Event(
            #     name = form.cleaned_data['event_name'],
            #     location = form.cleaned_data['event_location'],
            #     date_of_event = form.cleaned_data['event_date'],
            #     activity = form.cleaned_data['event_activity'],
            # )
            # mod_entry.save()
            form.save()
            return redirect('/locations')


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
