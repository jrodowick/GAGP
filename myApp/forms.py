from django import forms
from django.forms import Form, ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import datetime
from django.forms.widgets import SelectDateWidget
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

class EventForm(forms.Form):
    event_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
        'class':'form-control',
        'type':'text',
        'placeholder':'Give your activity a title!'
        })
    )
    event_location = forms.ModelChoiceField(
        queryset = Location.objects.all(),
        empty_label = 'Please choose location',
        to_field_name = 'name',
        widget = forms.Select(attrs={
            'class':'form-signin'
        })
    )
    event_date = forms.DateField(
        widget = SelectDateWidget(
            empty_label = ('Choose Year','Choose Month','Chose Day'),
        ),

    )
    event_activity = forms.ChoiceField(
        choices = EVENT_CHOICES,
        widget = forms.Select(attrs={
            'class':'form-signin',
            'placeholder':'Choose a sport'
        })
    )




    # event_location = forms.ChoiceField(
    #     required=True,
    #     choices = ['1','2','3'],
    #     label = 'Location'
    # )

    # def __init__(self, *args, **kwargs):
    #     super(EventForm, self).__init__(*args, **kwargs)
    #     self.fields['event_location'].choices = [(x[1]) for x in Location.objects.all().values_list()]
