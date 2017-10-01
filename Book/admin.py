from django.contrib import admin

# Register your models here.

from .models import Book, Author

# Register your models here.

admin.site.register(Book)
admin.site.register(Author)