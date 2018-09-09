from django import forms
from django.forms import Form
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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

    
