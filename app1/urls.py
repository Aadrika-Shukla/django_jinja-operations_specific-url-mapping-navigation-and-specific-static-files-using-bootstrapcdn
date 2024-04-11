'''specific url mapping for app1'''
from django.urls import path
from app1.views import *
app_name='app1'
urlpatterns=[
    path('bootfirst_cdn/',bootfirst_cdn,name='bootfirst_cdn'),
]