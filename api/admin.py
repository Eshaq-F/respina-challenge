from django.contrib import admin
from .models import Book, Author


# Set extra options for Book Model in Admin pages.
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category')
    readonly_fields = ('code',)
    list_filter = ['author']  # A filter by authors between books.


# A class to give more information about author to site's Admin.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'count_books')


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
