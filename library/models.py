from datetime import date
from django.db.models import (
    CharField,
    DecimalField,
    ForeignKey,
    CASCADE,
    TextField,
    IntegerField,
    DateField,
    ImageField,
    SET_NULL,
    Model,
)

from user.models import User


class Author(Model):
    full_name = CharField(max_length=255)

    def __str__(self):
        return self.full_name


class Genre(Model):
    name = CharField(max_length=64)

    def __str__(self):
        return self.name


class Book(Model):
    author = ForeignKey(Author, on_delete=CASCADE, related_name="books")
    genre = ForeignKey(Genre, on_delete=SET_NULL, related_name="genres", null=True, blank=True)
    title = CharField(max_length=255)
    description = TextField(null=True)
    length = IntegerField()
    published_date = IntegerField()
    created_date = DateField(default=date.today)
    copies_sold = IntegerField(default=0)
    price = IntegerField()
    discount = IntegerField(default=0, max=100)
    cover = ImageField(upload_to="book_covers/")

    def __str__(self):
        return self.title


class Rating(Model):
    rating = DecimalField(max_digits=2, decimal_places=1)
    user = ForeignKey(User, on_delete=CASCADE, related_name="ratings")
    book = ForeignKey(Book, on_delete=CASCADE, related_name="ratings")

    def __str__(self):
        return f"{self.user.name} - {self.book.title} ({self.rating})"
