from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout

from models import *
from forms import *

import datetime


@login_required
def game(request):
    if request.session.has_key('message'):
        message = request.session['message']
    else:
        message = ''
    try:
        set = Set.objects.get(pk=request.user.userprofile.toanswer)
    except ObjectDoesNotExist:
        request.session['completed'] = "You have finished answering all the questions. Thank you for your time."
        return redirect(reverse('mainapp:logout'))
    return render(request, template_name='game.html', context={'i': set, 'message': message, 'user': request.user})


def responses(request):
    if request.method == 'POST':
        choicepk = request.POST['pk']
        set = Set.objects.get(pk=choicepk)
        ans = request.POST[str(set.id)]
        choice = Choice()
        choice.choiceset = set
        choice.choicemade = ans
        choice.timestamp = datetime.datetime.now()
        choice.choiceuser = request.user.userprofile
        choice.save()
        request.user.userprofile.toanswer = int(choicepk)+1
        request.user.userprofile.save()
        request.session['message'] = "Choices submitted for {}".format(request.user.username)
        return redirect(reverse('mainapp:game'))
    else:
        return redirect(reverse('mainapp:game'))


def loginpage(request):
    if request.session.has_key('message'):
        message = request.session['message']
    else:
        message = ''
    if request.method == 'POST':
        logform = Loginform(request.POST)
        if logform.is_valid():
            user = authenticate(username=logform.cleaned_data['username'], password=logform.cleaned_data['password'])
            if user is not None:
                if not hasattr(user, 'userprofile'):
                    profile = Userprofile()
                    profile.user = user
                    profile.save()
                login(request, user)
                return redirect(reverse('mainapp:game'))
            else:
                message = "Please check login credentials"
                return render(request, 'login.html', {'logform': logform, 'message':message})
    else:
        logform = Loginform()
        return render(request, 'login.html', {'logform': logform, 'message':message})


@login_required
def logoutpage(request):
    if request.session.has_key('completed'):
        message = request.session['completed']
    else:
        message = request.user.username + "has been logged out. Thank you for your time."
    logout(request)
    logform = Loginform()
    return render(request, 'login.html', {'logform': logform, 'message': message})
