from django.conf.urls import url, include
from django.contrib import admin
from django.shortcuts import render
# from contents import views
from . import views

urlpatterns = [
    url(r'signup/', views.signup, name='signup'),
    # url(r'sex/', views.sex, name = 'sex'),
]
