from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'form/', views.data_form, name = 'form'),
    url(r'myblog/', views.myblog, name = 'myblog'),
    url(r'latestblog/', views.latestblog, name = 'latestblog'),
    url(r'(?P<id>\d+)/delete/$', views.delete, name='delete'),
    url(r'(?P<id>\d+)/edit/$', views.edit, name='edit'),
]