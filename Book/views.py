from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Author, Book
from django.template import loader
from django.views import generic
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm

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

def view_favourite(Request):
    template = loader.get_template('Author/Home.html')
    all_books = Book.objects.all()
    context = \
        {
            'all_books': all_books,
        }
    return HttpResponse(template.render(context, Request))


class UserFormView(View):
    form_class = UserForm
    template_name = 'Author/register.html'
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username'];
            password = form.cleaned_data['password'];
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password= password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('Book:Home_')
        return render(request, self.template_name, {'form': form})


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                #albums = Author.objects.filter(user=request.user)
                return render(request, 'Author/Home.html')#, {'albums': albums})
            else:
                return render(request, 'Author/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'Author/login.html', {'error_message': 'Invalid login'})
    return render(request, 'Author/login.html')