from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'/form/', views.data_form, name = 'form'),
    url(r'/myblog/', views.myblog, name = 'myblog'),
]