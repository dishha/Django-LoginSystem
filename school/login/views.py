# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


# Create your views here.
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.db.models import Q
from .forms import SignUpForm
from django.contrib.auth.models import User


def login_user(request):
	if request.method="POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
	    	login(request, user)
		    # Redirect to a success page.
		    return render(request, 'auth_user/base.html')
		    ...
		else:
		    # Return an 'invalid login' error message.
		    ...
		    return render(request,'auth_user/login.html', {'error_message': 'Invalid login'})
    return render(request, 'auth_user/login.html')

def logout_view(request):
    logout(request)
    # Redirect to a success page.
    form = SignUpForm(request.POST or None)
    context = {
        "form": forms,
    }
    return render(request, 'auth_user/login.html', context)