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
)

from configs.models import BaseModel
from user.models import User


class Author(BaseModel):
    first_name = CharField(max_length=255)
    last_name = CharField(max_length=255)
    birth_date = DateField()
    death_date = DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Genre(BaseModel):
    name = CharField(max_length=64)

    def __str__(self):
        return self.name


class Book(BaseModel):
    author = ForeignKey(Author, on_delete=CASCADE, related_name="books")
    genre = ForeignKey(Genre, on_delete=SET_NULL, related_name="genres", null=True, blank=True)
    title = CharField(max_length=255)
    description = TextField(null=True, blank=True)
    length = IntegerField()
    published_date = DateField()
    created_date = DateField(default=date.today)
    copies_sold = IntegerField(default=0)
    price = DecimalField(max_digits=6, decimal_places=2)
    discount = IntegerField(default=0)
    cover = ImageField(upload_to="books/covers/")

    def __str__(self):
        return self.title


class Rating(BaseModel):
    rating = DecimalField(max_digits=2, decimal_places=1)
    user = ForeignKey(User, on_delete=CASCADE, related_name="ratings")
    book = ForeignKey(Book, on_delete=CASCADE, related_name="ratings")

    def __str__(self):
        return f"{self.user.name} - {self.book.title} ({self.rating})"
