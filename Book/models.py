from django.db import models

# Create your models here.

class Author(models.Model):
    Name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.Name + ' ')
    
class Book(models.Model):
    Author_ID = models.ForeignKey(Author,on_delete=models.CASCADE)
    Title = models.CharField(max_length=100)
    def __str__(self):
        return self.Author_ID.__str__()+' - ' + self.Title + ' '


