from django.db import models

class Library(models.Model):
    book_title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publication_date = models.DateField()
    genre = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    num_pages = models.IntegerField()
    language = models.CharField(max_length=255)
    rating = models.FloatField()
    available = models.BooleanField()

