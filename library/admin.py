from django.contrib import admin

from library.models import Author, Book, Genre, Rating


class GenreAdmin(admin.ModelAdmin):
    model = Genre
    list_display = ("id", "name")


class AuthorAdmin(admin.ModelAdmin):
    model = Author
    list_display = ("id", "first_name", "last_name")


class BookAdmin(admin.ModelAdmin):
    model = Book
    list_display = ("id", "title", "genre", "price", "copies_sold", "published_date")


admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Rating)
