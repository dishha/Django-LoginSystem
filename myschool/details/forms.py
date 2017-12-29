from django import forms
from django.db import models


class TeacherForm(forms.ModelForm):
	FirstName= forms.CharField(widget=forms.TextInput(attrs={'class':'form-inline','type':'text','placeholder':'First name'}))
	LastName=forms.CharField(widget=forms.TextInput(attrs={'class':'form-inline','type':'text','placeholder':'Last name'}))
	Email=forms.EmailField(widget=forms.EmailInput(attrs={'type':'text','placeholder':'Email'}))
	Username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-inline','type':'text','placeholder':'Username'}))
	branch=forms.CharField(widget=forms.TextInput(attrs={'class':'form-inline','type':'text','placeholder':'Username'}))

	class Meta:
		model=Teacher
		fields=["FirstName","LastName","Email","Username","branch"]

class StudentForm(forms.ModelForm):
	FirstName= forms.CharField(widget=forms.TextInput(attrs={'class':'form-inline','type':'text','placeholder':'First name'}))
	LastName=forms.CharField(widget=forms.TextInput(attrs={'class':'form-inline','type':'text','placeholder':'Last name'}))
	Email=forms.EmailField(required=True,widget=forms.EmailInput(attrs={'type':'text','placeholder':'Email'}))
	Username=forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-inline','type':'text','placeholder':'Username'}))
	branch=forms.CharField(widget=forms.TextInput(attrs={'class':'form-inline','type':'text','placeholder':'Username'}))
	RollNumber=forms.IntegerField()

	class Meta:
		model=Student
		fields=["FirstName","LastName","Email","Username","branch","RollNumber"]

	














