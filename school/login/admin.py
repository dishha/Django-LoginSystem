# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
import models

# Register your models here.

class SignUpAdmin(admin.ModelAdmin):
	list_display=["__unicode__","timestamp","updated"]
	form=SignUpForm

admin.site.register(SignUp,SignUpAdmin)

class TeacherAdmin(admin.ModelAdmin):
	list_display=["nameT","updated"]

admin.site.register(Teacher,TeacherAdmin)

class StudentAdmin(admin.ModelAdmin):
	list_display=["nameS","updated"]

admin.site.register(Student,StudentAdmin)





