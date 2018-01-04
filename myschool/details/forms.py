from django import forms
from django.db import models
from .models import(Teacher,Student,cl)

class TeacherForm(forms.ModelForm):
	class Meta:
		model=Teacher
		fields=('name_T','emails_T','hw','branch')

class StudentForm(forms.ModelForm):
	FirstName= forms.CharField(widget=forms.TextInput(attrs={'class':'form-inline','type':'text','placeholder':'First name'}))
	LastName=forms.CharField(widget=forms.TextInput(attrs={'class':'form-inline','type':'text','placeholder':'Last name'}))
	Email=forms.EmailField(required=True,widget=forms.EmailInput(attrs={'type':'text','placeholder':'Email'}))
	Username=forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-inline','type':'text','placeholder':'Username'}))
	branch=forms.CharField(widget=forms.TextInput(attrs={'class':'form-inline','type':'text','placeholder':'branch'}))
	RollNumber=forms.IntegerField()

	class Meta:
		model=Student
		fields=["FirstName","LastName","Email","Username","RollNumber","branch"]

	














