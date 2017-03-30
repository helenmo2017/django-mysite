from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpRequest
from django.template import RequestContext
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm

def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/index/')
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')

    user = auth.authenticate(username = username, password = password)

    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect('/index/')
    else:
        return render(request,'login.html', locals())

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/index/')

def index(request):
    return render_to_response('index.html', RequestContext(request, locals()))

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return HttpResponseRedirect('/accounts/login/')
    else:
        form = UserCreationForm()
    return render(request,'register.html',locals())