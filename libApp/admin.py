from django.contrib import admin
from libApp.models import Library

# Register your models here.
class LibraryDetail(admin.ModelAdmin):
    myList=['book_title','author','publication_date','genre','publisher','num_pages','language','rating','available']

admin.site.register(Library,LibraryDetail)