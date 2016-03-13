from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

TYPE = (
    ('Driver', 'Driver'),
    ('Passenger','Passenger'),
)


class Location(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

class UserProfile(models.Model):
    user = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    #TODO


     # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user



class Trip(models.Model):
    key = models.AutoField(primary_key=True)
    user = models.CharField(max_length=200)
    name =  models.CharField(max_length=200)
    origin = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    date = models.DateField(null=True)
    date_posted = models.DateTimeField(null=True)
    active = models.BooleanField(default=True)
    num_passengers = models.IntegerField(default=0)
    msg = models.CharField(max_length=200)
    looktype = models.CharField(max_length=200)









