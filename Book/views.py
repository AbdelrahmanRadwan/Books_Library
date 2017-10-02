from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from .models import Author, Book
from django.template import loader

# Create your views here.
def index(Request):
    all_authors = Author.objects.all()
    html ="<h1>Hello World from home</h1><br>"
    for author in all_authors:
        link = 'http://127.0.0.1:8000/home/' + str(author.pk)+ '/'
        html += r'<a href= "'+ link + '">' + author.Name + '</a><br>'
    return HttpResponse(html)

def view_author(Request,view_author):
    return HttpResponse("<h2>Imformation about Abuthor number: "+ str(view_author)
                        +"</h2>")