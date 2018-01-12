from django.conf.urls import url
from django.contrib import admin
from .views import (Teacher_registration,Student_registration,student_details,student_list,student_update,student_delete,teacher_details,teacher_list,teacher_update,teacher_delete,addHomework)

urlpatterns =[
url(r'^teacher/$', Teacher_registration),
url(r'^student/$', Student_registration),
url(r'^student/(?P<id>\d+)$',student_details,name='detail'),
url(r'^student/list/$', student_list, name='list'),
url(r'^student/(?P<id>\d+)/edit/$', student_update, name='update'),
url(r'^student/(?P<id>\d+)/delete/$', student_delete),

url(r'^teacher/(?P<id>\d+)$',teacher_details,name='detail'),
url(r'^teacher/list/$', teacher_list, name='list'),
url(r'^teacher/(?P<id>\d+)/edit/$', teacher_update, name='update'),
url(r'^teacher/(?P<id>\d+)/delete/$', teacher_delete),

url(r'^teacher/addhw/$',addHomework,name='hw'),

]

