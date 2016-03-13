from django.contrib import admin
from main.models import UserProfile, Trip, Location
# Register your models here.


admin.site.register(UserProfile)
admin.site.register(Location)
admin.site.register(Trip)
