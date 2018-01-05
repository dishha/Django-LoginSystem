# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .forms import (StudentForm, TeacherForm)
from .models import (Teacher, Student , Class)
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404


# Create your views here.

def Teacher_registration(request):
	form =TeacherForm(request.POST or None, request.FILES or None)
	if form.is_valid():
			form.save()
			instance = form.save(commit=False)
			instance.save()
			return HttpResponse("success")
	context ={
		"form": TeacherForm,
	}
	return render(request,"teacher_form.html",context)

def Student_registration(request):
	form =StudentForm(request.POST or None,request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponse("success")
	
	
	context ={
		"form": StudentForm,
	}
	return render(request,"student_form.html",context)



def student_details(request,id=None):
	instance=get_object_or_404(Student,id=id)
	context ={
	"title":instance.name_S,
	"instance":instance
		}

	return render(request,"student_details.html",context)

def student_list(request):
	queryset=Student.objects.all().order_by("-timestamp")
	context ={
	"object_list":queryset,
		"title":"list"
		}

	return render(request,"student_list.html",context)

def student_update(request,id=None):
	instance = get_object_or_404(Student, id=id)
	form =StudentForm(request.POST or None ,request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit = False)
		instance.save()
		return HttpResponse("Succesfully Updated")
	
	context ={
	"name_S":instance.name_S,
	"instance": instance,
	"form": form,
	}
	return render(request,"student_form.html",context)

def student_delete(request,id=None):
	instance = get_object_or_404(Student, id=id)
	instance.delete()
	return HttpResponse("Succesfully Deleted")

def teacher_details(request,id=None):
	instance=get_object_or_404(Teacher,id=id)
	context ={
	"title":instance.name_T,
	"instance":instance
		}

	return render(request,"teacher_details.html",context)

def teacher_list(request):
	queryset=Teacher.objects.all().order_by("-timestamp")
	context ={
	"object_list":queryset,
		"title":"list"
		}

	return render(request,"teacher_list.html",context)

def teacher_update(request,id=None):
	instance = get_object_or_404(Teacher, id=id)
	form =TeacherForm(request.POST or None ,request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit = False)
		instance.save()
		return HttpResponse("Succesfully Updated")
	
	context ={
	"name_S":instance.name_T,
	"instance": instance,
	"form": form,
	}
	return render(request,"teacher_form.html",context)

def teacher_delete(request,id=None):
	instance = get_object_or_404(Teacher, id=id)
	instance.delete()
	return HttpResponse("Succesfully Deleted")