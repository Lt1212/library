from django.contrib import admin

# Register your models here.

from .models import Author, Genre, Book, BookInstance


admin.site.register(Genre)

class BooksInline(admin.TabularInline):
    """Defines format of inline book insertion (used in AuthorAdmin)"""
    model = Book

# Register the Admin classes for Book using the decorator
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title','imprint', 'isbn','author', 'display_genre')
    inlines = [BooksInstanceInline]

# Register the Admin classes for BookInstance using the decorator

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id') 
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
            'fields': ('book', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'borrower', 'due_back' )
        }),
    )

# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_of_birth', 'date_of_death', 'sex','image')
    fields = ['name', ('date_of_birth', 'date_of_death'),'sex','image', 'summary']
    inlines = [BooksInline]

# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)