from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

from models import *
from forms import *

import datetime


def game(request):
        sets = Set.objects.all()
        if request.session.has_key('message'):
            message = request.session['message']
        else:
            message = ''
        return render(request, template_name='game.html', context={'sets':sets, 'message':message, 'user':request.user})


def responses(request):
    if request.method == 'POST':
        choiceset = Set.objects.all()
        print request.POST
        for i in choiceset:
            ans = request.POST[str(i.id)]
            choice = Choice()
            choice.choiceset = i
            choice.choicemade = ans
            choice.timestamp = datetime.datetime.now()
            choice.choiceuser = request.user
            choice.save()
            request.session['message'] = "Choices submitted for {}".format(request.user.username)
        return redirect(reverse('mainapp:game'))
    else:
        return redirect(reverse('mainapp:game'))


def loginpage(request):
    if request.method == 'POST':
        logform = Loginform(request.POST)
        print "1"
        if logform.is_valid():
            user = authenticate(username=logform.cleaned_data['username'], password=logform.cleaned_data['password'])
            print user
            print "2"
            if user is not None:
                login(request, user)
                return redirect(reverse('mainapp:game'))
            else:
                message = "Please check login credentials"
                return render(request, 'login.html', {'logform': logform, 'message':message})
    else:
        logform = Loginform()
        return render(request, 'login.html', {'logform': logform})
