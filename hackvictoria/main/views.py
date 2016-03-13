from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from main.forms import UserForm, UserProfileForm
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
# Create your views here.

def mainpage(request):
    #FIX TO REDIRECT
    context = RequestContext(request)
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print user_form.errors
    else:
        user_form = UserForm()

    return render_to_response('main/main.html',{'user_form': user_form, 'registered': registered}, context)

def login_user(request):
    context = RequestContext(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                #LOGIN
                return HttpResponseRedirect('/userpage/')

            else:
                return HttpResponse("Account is inactive")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            #FIX this?
            return HttpResponse("Invalid login.")

    else:
        return render_to_response('main/login.html', {}, context)

def userpage(request):
    context = RequestContext(request)
    if not request.user.is_authenticated():
         return HttpResponseRedirect('/login/')
    else:
        return render_to_response('main/user_page.html',{}, context)

def editprofile(request):
    context = RequestContext(request)
    if not request.user.is_authenticated():
         return HttpResponseRedirect('/login/')
    else:
        if request.method == 'POST':
            form = UserProfileForm(data=request.POST)
            if form.is_valid():
                user = form.save()
                user.save()
            else:
                print form.errors
        else:
            user_form = UserForm()
            return render_to_response('main/edit_profile.html',{}, context)

def addtrip(request):
    context = RequestContext(request)
    if not request.user.is_authenticated():
         return HttpResponseRedirect('/login/')
    else:
        return render_to_response('main/add_trip.html',{}, context)

