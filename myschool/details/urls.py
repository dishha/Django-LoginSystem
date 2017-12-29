from django.conf.urls import url
from django.contrib import admin
from .views import (Teacher_registration,Student_registration)

urlpatterns =[
url(r'^teacher/$', Teacher_registration),
url(r'^student/$', Student_registration),
]