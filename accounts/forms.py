from copyreg import remove_extension
from os import remove
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
        help_texts = {
            'username': None,
        }
        


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username' ,'email', 'first_name', 'last_name']
        
        help_texts = {
            'username': None,
        }



class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['address', 'phone_number', 'profile_image']
