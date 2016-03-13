from django import forms
from main.models import UserProfile, Trip
from django.contrib.auth.models import User
import datetime


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')



class UserProfileForm(forms.ModelForm):
    #TODO
    class Meta:
        model = UserProfile


class Trip(forms.ModelForm):

    class Meta:
        model = Trip
