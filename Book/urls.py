from django.conf.urls import url
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^$', views.index),

    url(r'^(?P<view_author>[0-9]+)/$', views.view_author, name="Author"),

]

