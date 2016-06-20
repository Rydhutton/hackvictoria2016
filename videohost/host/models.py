from __future__ import unicode_literals

from django.db import models
import uuid
import os
# Create your models here.

def keygen():
        key = uuid.uuid4()
        return int(key.int & 0xFFFFFF)


class Video(models.Model):
    id = models.IntegerField(primary_key=True, default=keygen, editable=False)
    bucket = models.CharField(max_length=255,  default='EMPTY')
    path = models.CharField(max_length=1000, unique=True, default='EMPTY')
    name = models.CharField(max_length=255, default='EMPTY')
    extension = models.CharField(max_length=10, default='EMPTY')

    def __unicode__(self):
       return  self.name

