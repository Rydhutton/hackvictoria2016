from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

TYPE = (
    'Driver',
    'Passenger',
    )
LOCATION_CHOICES = (
    'Victoria',
)

class UserProfile(models.Model):

    user = models.OneToOneField(User)

    #TODO
    #picture = models.ImageField(upload_to='profile_images', blank=True)
    age = models.IntegerField(default=0)
    location = models.CharField(max_length=200)
    joined = models.DateTimeField()
    type = models.CharField(max_length=200,choices=TYPE)


     # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username



class Trip(models.Model):
    user = models.manyToOne(UserProfile)
    origin = models.CharField(max_length=200,choices= LOCATION_CHOICES)
    destination = models.CharField(max_length=200,choices= LOCATION_CHOICES)
    date = models.DateTimeField()
    date_posted = models.DateTimeField()
    active = models.BooleanField(defualt=True)
    num_passengers = models.IntegerField(default=0)
    msg = models.CharField(max_length=200)
    looktype = models.CharField(max_length=200,choices=TYPE)








