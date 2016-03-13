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
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #TODO
    #picture = models.ImageField(upload_to='profile_images', blank=True)
    displayname = models.CharField(max_length=30,null=True )
    age = models.IntegerField(default=0)
    location = models.CharField(max_length=200,null=True )
    joined = models.DateTimeField(null=True)
    type = models.CharField(max_length=200,choices=TYPE, default=TYPE[0])
    about = models.CharField(max_length=200, null=True)


     # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username



class Trip(models.Model):
    #user = models.ManyToMany(UserProfile)
    origin = models.OneToOneField(User, related_name='location_origin')
    destination = models.OneToOneField(User, related_name='location_dest')
    date = models.DateTimeField(null=True)
    date_posted = models.DateTimeField(null=True)
    active = models.BooleanField(default=True)
    num_passengers = models.IntegerField(default=0)
    msg = models.CharField(max_length=200)
    looktype = models.CharField(max_length=200,choices=TYPE, default=TYPE[0])









