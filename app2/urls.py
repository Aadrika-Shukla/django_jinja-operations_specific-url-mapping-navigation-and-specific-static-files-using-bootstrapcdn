'''specific url mapping for app2'''
from django.urls import path
from app2.views import *
app_name='app2'
urlpatterns=[
    path('bootsecond_cdn/',bootsecond_cdn,name='bootsecond_cdn'),
]