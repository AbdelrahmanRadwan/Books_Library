from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from .models import Author, Book
from django.template import loader

# Create your views here.
def view_home(Request):
    all_authors = Author.objects.all()
    all_books = Book.objects.all()
    template = loader.get_template('Author/Home.html')
    context = \
    {
        'all_authors' : all_authors,
        'all_books' : all_books,
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

def view_book(Request, view_book):
    specific_Book = Book.objects.get(pk=view_book)
    template = loader.get_template('Author/Book.html')
    context = \
        {
            'Book': specific_Book,
        }
    return HttpResponse(template.render(context, Request))

