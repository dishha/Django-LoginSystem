# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from details.models import Teacher , Student , cl

# Register your models here.
admin.site.register(cl)
admin.site.register(Teacher)
admin.site.register(Student)