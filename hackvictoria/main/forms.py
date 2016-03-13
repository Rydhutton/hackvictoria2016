from django import forms
from main.models import Trip, Location
from django.contrib.auth.models import User
from datetimewidget.widgets import DateWidget
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



class TripForm(forms.ModelForm):
    name = forms.CharField(max_length=200)
    origin = forms.CharField(max_length=200)
    destination = forms.CharField(max_length=200)
    date = forms.DateField(widget=DateWidget(usel10n=True, bootstrap_version=3))
    passengers = forms.IntegerField()
    msg = forms.CharField(max_length=200)
    looktype = forms.CharField(max_length=200)

    class Meta:
        model = Trip
        fields = ('name', 'origin', 'destination', 'date', 'passengers', 'msg', 'looktype')
