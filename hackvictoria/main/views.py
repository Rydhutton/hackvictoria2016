from django.shortcuts import render
from django.http import HttpResponse
from main.forms import UserForm, UserProfileForm
from django.template import RequestContext
from django.shortcuts import render_to_response
# Create your views here.

def mainpage(request):
    context = RequestContext(request)

    registered = False

    if request == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user =user_form.save()
            user.set_password(user.password)
            user.save()
        else:
            print user_form.errors
    else:
        user_form = UserForm()

    return render_to_response('main/main.html',{'user_form': user_form, 'registered': registered}, context)