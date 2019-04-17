"""Comienzo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.shortcuts import render
from contents import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url( r'^login/$',auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    url( r'^logout/$',auth_views.LogoutView.as_view(template_name="home.html"), name="logout"),
    url( r'^password_change/$',auth_views.PasswordChangeView.as_view(template_name="password_change.html"), name="password_change"),
    # url( r'^password_change_done/',auth_views.PasswordChangeDoneView.as_view(template_name="password_change_done.html")),
    #url(r'password_change_done/',auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html')),
    url(r'password_change_done/',auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html')),
    url(r'^user/', include('user.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'', views.home, name = 'home'),
]
