from django import forms
from django.forms import Form, ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.admin.widgets import AdminTimeWidget

import datetime
from .models import *

class RegistrationForm(UserCreationForm):
    username = forms.CharField(
        widget = forms.TextInput(attrs={
        'class':'form-control',
        'type':'username',
        'placeholder':'Username',
        })
    )
    email = forms.EmailField(
        label = 'Email',
        required = True,
        widget = forms.TextInput(attrs={
        'class':'form-control',
        'type':'email',
        'placeholder':'Email address',
        })
    )
    password1 = forms.CharField(
        widget = forms.TextInput(attrs={
        'class':'form-control',
        'type':'password',
        'placeholder':'Password',
        })
    )
    password2 = forms.CharField(
        widget = forms.TextInput(attrs={
        'class':'form-control',
        'type':'password',
        'placeholder':'Confirm Password',
        })
    )

    def save(self, commit = True):
        return User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class EventForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date_of_event'].widget.attrs.update({'class':'form-control'})
        self.fields['time_of_event'].widget.attrs.update({'class':'form-control'})

    class Meta:
        model = Event
        fields = ['name','location','activity','date_of_event', 'time_of_event']
        widgets = {
            'date_of_event': DateInput(),
            'time_of_event': TimeInput(),
            'name': forms.TextInput(attrs={
                'class':'form-control'
            }),
            'location': forms.Select(attrs={
                'class':'form-control'
            }),
            'activity': forms.Select(attrs={
                'class':'form-control'
            }),
        }

    def clean(self):
        date = self.cleaned_data['date_of_event']
        if date < datetime.date.today():
            raise forms.ValidationError("Date of event cannot be in the past!")

    # event_name = forms.CharField(
    #     required=True,
    #     widget=forms.TextInput(attrs={
    #     'class':'form-control',
    #     'type':'text',
    #     'placeholder':'Give your activity a title!'
    #     })
    # )
    # event_location = forms.ModelChoiceField(
    #     queryset = Location.objects.all(),
    #     empty_label = 'Please choose location',
    #     to_field_name = 'name',
    #     widget = forms.Select(attrs={
    #         'class':'form-signin'
    #     })
    # )
    # event_date = forms.DateField(
    #     widget = {
    #         'event_date':forms.widget.DateInput(attrs={
    #             'type':'date',
    #         })
    #     }
    # )
    # event_activity = forms.ChoiceField(
    #     choices = EVENT_CHOICES,
    #     widget = forms.Select(attrs={
    #         'class':'form-signin',
    #         'placeholder':'Choose a sport'
    #     })
    # )
