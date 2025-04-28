import os
import pytest

from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APIClient

from library.models import Author, Book, Genre
from user.models import User


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def create_user():
    def make_user(**kwargs):
        user = User(**kwargs)
        user.set_password(kwargs["password"])
        user.save()
        return user

    return make_user


@pytest.fixture
def auth_client(create_user):
    user = create_user(
        name="Test User",
        email="user@example.com",
        password="Password123",
    )

    client = APIClient()
    client.force_authenticate(user=user)

    return client


@pytest.fixture
def author_data():
    return {
        "first_name": "John",
        "last_name": "Doe",
        "birth_date": "1970-01-01",
        "death_date": "2020-01-01",
    }


@pytest.fixture
def author(author_data):
    return Author.objects.create(**author_data)


@pytest.fixture
def genre_data():
    return {"name": "Fiction"}


@pytest.fixture
def genre(genre_data):
    return Genre.objects.create(**genre_data)


@pytest.fixture
def book_data(author, genre):
    image_path = os.path.join(os.path.dirname(__file__), "test_image.jpg")
    with open(image_path, "rb") as img_file:
        image_data = img_file.read()

    return {
        "title": "Test Book",
        "description": "A test book description",
        "author": author.id,
        "genre": genre.id,
        "length": 300,
        "published_date": "2022-01-01",
        "price": "29.99",
        "discount": 10,
        "cover": SimpleUploadedFile(
            name="test_image.jpg",
            content=image_data,
            content_type="image/jpeg",
        ),
    }


@pytest.fixture
def book(author, genre):
    return Book.objects.create(
        title="Test Book",
        description="A test book description",
        author=author,
        genre=genre,
        length=300,
        published_date="2022-01-01",
        price="29.99",
        discount=10,
        cover="books/covers/test_image.jpg",
    )
