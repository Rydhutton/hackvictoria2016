from django import forms
from main.models import UserProfile, Trip, Location
from django.contrib.auth.models import User
import datetime


TYPE = (
    ('Driver', 'Driver'),
    ('Passenger','Passenger'),
)


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')



class UserProfileForm(forms.ModelForm):
    #queryset=Location.objects.all()
    #user = forms.ModelMultipleChoiceField(queryset=Location.objects.all())
    age = forms.IntegerField()
    location = forms.ModelChoiceField(queryset=Location.objects.all())
    joined = datetime.datetime.now()
    type = forms.ChoiceField(choices=TYPE)
    about = forms.CharField(widget = forms.Textarea)


    class Meta:
        model = UserProfile
        fields = ('age', 'location', 'type', 'about' )


class Trip(forms.ModelForm):

    class Meta:
        model = Trip
        fields = ()
