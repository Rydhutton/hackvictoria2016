from django.contrib import admin

# Register your models here.
from .models import Video


class VideoAdmin(admin.ModelAdmin):
    list_display = ['id', 'bucket', 'path', 'name', 'extension']

admin.site.register(Video, VideoAdmin)