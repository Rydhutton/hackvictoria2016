from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.core import serializers
from django.views.generic import FormView
from .forms import S3DirectUploadForm
from django.conf import settings
import boto
from models import Video
import os

# Create your views here.


def mainpage(request):
    return render(request, 'host/main.html')

def video(request, videoid):
    vid = Video.objects.filter(id=videoid)
    source = ''
    if vid:
        vid = vid[0]
        source = settings.AWS_DISTRIB_DIR + vid.path
    return render(request, 'host/video.html',{'video':vid, 'source':source} )


def embed(request, videoid):
    vid = Video.objects.filter(id=videoid)
    source = ''
    if vid:
        vid = vid[0]
        source = settings.AWS_DISTRIB_DIR + vid.path
    return render(request, 'host/embed.html',{'video':vid, 'source':source} )


def update(request):
    if request.user.is_authenticated():
        connect = boto.connect_s3(settings.AWS_ACCESS_KEY_ID, settings.AWS_SECRET_ACCESS_KEY)
        try:
            bucket = connect.get_bucket(settings.AWS_STORAGE_BUCKET_NAME, validate=True)
            keys =  bucket.list()

            #Update DB
            for key in keys:
                if not Video.objects.filter(path=key.name).exists():
                    fname = os.path.splitext(os.path.basename(key.name))[0]
                    x, file_extension = os.path.splitext(key.name)
                    video = Video(bucket=key.bucket.name, path=key.name, name=fname, extension=file_extension )
                    video.save()

        except boto.exception.S3ResponseError, e:
            HttpResponse(e);
    else:
         return HttpResponseRedirect('/login/')

    data = serializers.serialize("json", Video.objects.all())
    return HttpResponse(data)



def login_user(request):
    context = RequestContext(request)
    if request.user.is_authenticated():
         return HttpResponseRedirect('/')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)

            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/userpage')

                else:
                    return HttpResponse("Account is inactive")
            else:
                return HttpResponse("Invalid login.")

        else:
            return render_to_response('host/login.html', {}, context)

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')

def userpage(request):
    context = RequestContext(request)
    if not request.user.is_authenticated():
         return HttpResponseRedirect('/login/')

    if request.method == 'POST':
        form = S3DirectUploadForm()
        #TODO add to database
    else:
        form = S3DirectUploadForm()


    return render_to_response('host/userpage.html', {'form':form } ,  context)


def dmca(request):
    return render(request, 'host/dmca.html')

def faq(request):
    return render(request, 'host/faq.html')

def tos(request):
    return render(request, 'host/tos.html')

def contact(request):
    return render(request, 'host/contact.html')