from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from main.forms import UserForm, TripForm
from main.models import UserProfile, User, Location, Trip
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
import datetime

# Create your views here.

def mainpage(request):
    #FIX TO REDIRECT
    context = RequestContext(request)
    if request.user.is_authenticated():
         return HttpResponseRedirect('/main/userpage/')
    else:
        if request.method == 'POST':
            user_form = UserForm(data=request.POST)
            if user_form.is_valid() and (request.POST['password'] == request.POST['check']):
                user = user_form.save()
                user.set_password(user.password)
                user.save()
                userprofile = UserProfile()
                userprofile.user = user.username
                userprofile.email = user.email
                userprofile.joined = datetime.datetime.now()
                userprofile.save()

                user = authenticate(username=user_form.cleaned_data['username'],
                                    password=user_form.cleaned_data['password'],
                                    )
                login(request, user)

                return HttpResponseRedirect('/main/userpage/')

            else:
                print user_form.errors
        else:
            user_form = UserForm()



    return render_to_response('main/main.html',{'form': user_form,}, context)

def login_user(request):
    context = RequestContext(request)
    if request.user.is_authenticated():
         return HttpResponseRedirect('/main/userpage/')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)

            if user:
                if user.is_active:
                    login(request, user)
                    #LOGIN
                    return HttpResponseRedirect('/main/userpage/')

                else:
                    return HttpResponse("Account is inactive")
            else:
                print "Invalid login details: {0}, {1}".format(username, password)
                #FIX this?
                return HttpResponse("Invalid login.")

        else:
            return render_to_response('main/login.html', {}, context)

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/main/')

def userpage(request):
    context = RequestContext(request)
    trips = None
    results = None
    usertrip=None
    if not request.user.is_authenticated():
         return HttpResponseRedirect('/main/login/')
    else:
        trips = Trip.objects.filter(user=request.user).values()
        tripid = request.GET.get('trip')
        if tripid != None:
            tripid = request.GET.get('trip')
            usertrip = Trip.objects.get(key=tripid)
            #print usertrip.date, usertrip.looktype, usertrip.origin, usertrip.destination

            type = 'Driver'
            if usertrip.looktype == 'Driver':
                type = 'Passenger'

            #print type

            #print usertrip.date, type, usertrip.origin,usertrip.destination

            qs = Trip.objects.exclude(user=request.user)
            qs = qs.filter(date=usertrip.date, looktype=type, origin=usertrip.origin, destination=usertrip.destination)
            results = qs.values()



        return render_to_response('main/user_page.html',{'trips':trips,'results':results, 'usertrip':usertrip }, context)


def addtrip(request):
    context = RequestContext(request)
    if not request.user.is_authenticated():
         return HttpResponseRedirect('/main/login/')
    else:
        locations = Location.objects.all()
        if request.method == 'POST':
            form = TripForm(data=request.POST)
            if form.is_valid():
                trip = form.save(commit=False)
                trip.user = request.user
                trip.date_posted = datetime.datetime.now()
                trip.save()
                return HttpResponseRedirect('/main/userpage/'+ trip.name)
            else:
                print form.errors
        else:
            form = TripForm()

        return render_to_response('main/add_trip.html',{'locations':locations, 'form':form}, context)

