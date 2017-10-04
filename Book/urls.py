from django.conf.urls import url
from django.contrib import admin
from . import views
urlpatterns = [
    #Local_Host/Home/
    url(r'^$', views.view_home),
    # Local_Host/Home/author/123
    url(r'^author/(?P<view_author>[0-9]+)/$', views.view_author, name="Author"),
    # Local_Host/Home/book/123
    url(r'^book/(?P<view_book>[0-9]+)/$', views.view_book, name="Book"),

]

