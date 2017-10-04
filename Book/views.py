from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from .models import Author, Book
from django.template import loader

# Create your views here.
def index(Request):
    all_authors = Author.objects.all()
    template = loader.get_template('Author/Home.html')
    context = \
    {
        'all_authors' : all_authors,
    }
    return HttpResponse(template.render(context, Request))

def view_author(Request,view_author):
    specific_Author = Author.objects.get(pk =view_author)
    template = loader.get_template('Author/Author.html')
    context = \
    {
        'Author' : specific_Author,
    }
    return HttpResponse(template.render(context, Request))
    '''return HttpResponse("<h2>Imformation about Abuthor number: "+ str(view_author)
                        +"</h2>")'''

