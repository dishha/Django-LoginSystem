# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from details.models import Teacher , Student , Class, Homework

# Register your models here.
admin.site.register(Class)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Homework)