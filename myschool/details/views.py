# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .forms import (StudentForm, TeacherForm)
from .models import (Teacher, Student)

# Create your views here.


def Teacher_registration(request):
	form =TeacherForm(request.POST or None,request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Successfully Registered")
		return HttpResponseRedirect(instance.get_absolute_url())
	
	
	context ={
		"form": TeacherForm,
	}
	return render(request,"teacher_form.html",context)

def Student_registration(request):
	form =StudentForm(request.POST or None,request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Successfully Registered")
		return HttpResponseRedirect(instance.get_absolute_url())
	
	
	context ={
		"form": StudentForm,
	}
	return render(request,"student_form.html",context)
	