from django.conf.urls import url
from django.contrib import admin

from login import views
app_name = 'login'

urlpatterns =[

    url(r'^login/$', views.login, name='login'),
    url(r'^$', views.logout, name='logout'),


    
    #url(r'^posts/$', "<appname>.views.<function_name>"),
]
