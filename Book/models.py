from django.db import models

# Create your models here.

class Author(models.Model):
    Name = models.CharField(max_length=100)
    
class Book(models.Model):
    Author_ID = models.ForeignKey(Author,on_delete=models.CASCADE)
    Title = models.CharField(max_length=100)


