from django.shortcuts import render, redirect, HttpResponse
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
    if(request.method == 'GET'):
        locations = Location.objects.all()
        return render(request, 'locations.html', {'locations':locations})

def local_event(request):
    if(request.method == 'POST'):
        events = Event.objects.all()
        results = []
        dict = {}

        for row in events:
            dict = row.asDict()
            dict['location'] = dict['location'].asDict()
            results.append(dict)

        response = json.dumps(results, default = str)
        return HttpResponse(response, content_type = 'application/json')

# def test_view(request):
#     if(request.method == 'GET'):
#         return render(request, 'test.html')
#
#
#     if(request.method == 'POST'):
#         events = Event.objects.all()
#         results = []
#         dict = {}
#
#         for row in events:
#             dict = row.asDict()
#             dict['location'] = dict['location'].asDict()
#             results.append(dict)
#
#         response = json.dumps(results, default = str)
#         return HttpResponse(response, content_type = 'application/json')

def events(request):
    events = Event.objects.all()
    if(request.method == 'POST'):
        form = EventForm(request.POST)
        if(form.is_valid()):
            mod_entry = Event(
                name = form.cleaned_data['event_name'],
                location = form.cleaned_data['event_location'],
                date_of_event = form.cleaned_data['event_date'],
                activity = form.cleaned_data['event_activity'],
            )
            mod_entry.save()

    else:
        form = EventForm()
    return render(request, 'events.html', {'form':form,'events':events})

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
