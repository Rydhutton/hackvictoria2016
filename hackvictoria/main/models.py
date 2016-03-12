from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User)

    #TODO
    #picture = models.ImageField(upload_to='profile_images', blank=True)


     # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username








