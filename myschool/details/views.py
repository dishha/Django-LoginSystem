# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .forms import (StudentForm, TeacherForm)
from .models import (Teacher, Student , cl)

# Create your views here.


def Teacher_registration(request):
	form =TeacherForm(request.POST or None,request.FILES or None)
	print "after form variable"
	
	branch1 = form['branch'].value() #foreignkey
	print branch1

	branch2 = cl.objects.get(branch=branch1) 
	print branch2
	branch_id=branch2.pk
	print branch_id	
	form.update(branch = 'branch_id')
	


	
	if form.is_valid():
			print "inside if block"
			
			
		

			

			form.save()

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
	