from django.conf.urls import url
from django.contrib import admin
from . import views

app_name = 'Book'

urlpatterns = \
    [
        #Local_Host/Home/
        url(r'^$', views.view_home, name= "Home_"),
        # Local_Host/Home/author/123
        url(r'^author/(?P<view_author>[0-9]+)/$', views.view_author, name="Author_"),
        # Local_Host/Home/book/123
        url(r'^book/(?P<view_book>[0-9]+)/$', views.view_book, name="Book_"),
        # Local_Host/Book_ID/favourite
        url(r'^book/favourite/$', views.view_favourite, name="Favourite_"),

    ]

