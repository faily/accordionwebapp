from django import forms
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core import serializers
from django.core.context_processors import csrf
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404, render, \
    redirect
from django.template import loader, RequestContext
from django.views.decorators.csrf import csrf_exempt

from accordion_app.models import *
from accordion_app.model_forms import *
from accordion_app.forms import *

#@login_required
def index(request):
    return render(request, "index.html", locals())
def useraccounts(request):
    return render(request, "useraccounts.html", locals())