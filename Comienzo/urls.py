
from django.conf.urls import url, include
from django.contrib import admin
from django.shortcuts import render
from contents import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url( r'^login/$',auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    url( r'^logout/$',auth_views.LogoutView.as_view(template_name="home.html"), name="logout"),
    url( r'^password_change/$',auth_views.PasswordChangeView.as_view(template_name="password_change.html"), name="password_change"),
    url(r'^contents/', include('contents.urls')),
    url(r'^user/', include('user.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'', views.home, name = 'home'),
]
