from django.conf.urls import url
from rango import views
from django.contrib import admin

urlpatterns = [
    url(r'^$', views.index, name='index'),
]