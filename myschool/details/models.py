# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.forms import ModelForm
# Create your models here.

class Class(models.Model):
	branch = models.CharField(max_length=10)

	def __str__(self):
		return self.branch

class Teacher(models.Model):
	name_T = models.CharField(max_length=50)
	emails_T= models.EmailField()
	branch=models.ForeignKey(Class,null=False)
	updated= models.DateTimeField(auto_now=True,auto_now_add=False)
	timestamp= models.DateTimeField(auto_now=False,auto_now_add=True)


	def __str__(self):
		return self.name_T

	class Meta:
		ordering =["-timestamp","-updated"]


class Student(models.Model):
	name_S= models.CharField(max_length=50)
	emails_S=models.EmailField()
	rollnumber=models.IntegerField()
	branch=models.ForeignKey(Class,null=False)
	updated= models.DateTimeField(auto_now=True,auto_now_add=False)
	timestamp= models.DateTimeField(auto_now=False,auto_now_add=True)


	def __str__(self):
		return self.name_S

	class Meta:
		ordering =["-timestamp","-updated"]

class Homework(models.Model):
	topic = models.CharField(max_length=50)
	questions=models.TextField()
	due_date=models.DateTimeField()
	updated= models.DateTimeField(auto_now=True,auto_now_add=False)
	timestamp= models.DateTimeField(auto_now=False,auto_now_add=True)

	def __str__(self):
		return self.topic

	class Meta:
		ordering =["-timestamp","-updated"]








			


	