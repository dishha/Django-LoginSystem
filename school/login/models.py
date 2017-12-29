# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class SignUp(models.Model):
	email= models.EmailField(max_length=250)
	username=models.CharField(max_length=100)
	timestamp=models.DateTimeField(auto_now=False, auto_now_add=True)
	updated=models.DateTimeField(auto_now=True,auto_now_add=False)

	def __unicode__(self):
		return self.username

	def __str__(self):
		return self.username

class Teacher(models.Model):
	nameT=models.CharField(max_length=20)
	cl = models.CharField(max_length=5)
	hw = models.TextField(max_length=500)

	def __unicode__(self):
		return self.nameT

class Student(models.Model):
	nameS=models.CharField(max_length=20)
	cl = models.CharField(max_length=5)
	RollNumber = models.IntegerField()

	def __unicode__(self):
		return self.nameS










