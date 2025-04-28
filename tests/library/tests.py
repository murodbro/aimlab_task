import pytest

from django.urls import reverse
from rest_framework import status

from library.models import Author, Book, Genre, Rating


@pytest.mark.django_db
def test_create_author(auth_client, author_data):
    url = reverse("create_author")

    response = auth_client.post(url, author_data, format="json")

    assert response.status_code == status.HTTP_201_CREATED
    assert response.data["first_name"] == author_data["first_name"]
    assert response.data["last_name"] == author_data["last_name"]


@pytest.mark.django_db
def test_list_authors(auth_client, author_data):
    url = reverse("create_author")

    auth_client.post(url, author_data, format="json")

    response = auth_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) > 0
    assert response.data[0]["first_name"] == author_data["first_name"]


@pytest.mark.django_db
def test_retrieve_author(auth_client, author):
    url = reverse("author_detail", kwargs={"id": author.id})

    response = auth_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response.data["first_name"] == author.first_name
    assert response.data["last_name"] == author.last_name


@pytest.mark.django_db
def test_update_author(auth_client, author):
    url = reverse("author_detail", kwargs={"id": author.id})
    new_data = {"first_name": "Updated", "last_name": "Author"}

    response = auth_client.patch(url, new_data, format="json")

    assert response.status_code == status.HTTP_200_OK

    assert response.data["first_name"] == new_data["first_name"]
    assert response.data["last_name"] == new_data["last_name"]

    author.refresh_from_db()

    assert author.first_name == new_data["first_name"]
    assert author.last_name == new_data["last_name"]


@pytest.mark.django_db
def test_delete_author(auth_client, author):
    url = reverse("author_detail", kwargs={"id": author.id})

    response = auth_client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert not Author.objects.filter(id=author.id).exists()


@pytest.mark.django_db
def test_create_book(auth_client, book_data):
    url = reverse("create_book")

    response = auth_client.post(url, book_data, format="multipart")
    print(response.data)

    assert response.status_code == status.HTTP_201_CREATED
    assert response.data["title"] == book_data["title"]
    assert response.data["description"] == book_data["description"]
    assert response.data["length"] == book_data["length"]
    assert Book.objects.count() == 1


@pytest.mark.django_db
def test_create_book_missing_required_fields(auth_client, book_data):
    url = reverse("create_book")

    invalid_data = book_data.copy()
    del invalid_data["title"]

    response = auth_client.post(url, invalid_data, format="multipart")

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "title" in response.data


@pytest.mark.django_db
def test_retrieve_book(auth_client, book):
    url = reverse("book_detail", kwargs={"id": book.id})

    response = auth_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response.data["title"] == book.title
    assert response.data["description"] == book.description


@pytest.mark.django_db
def test_update_book(auth_client, book):
    url = reverse("book_detail", kwargs={"id": book.id})
    update_data = {"title": "Updated Title", "description": "Updated description"}

    response = auth_client.patch(url, update_data, format="json")

    assert response.status_code == status.HTTP_200_OK
    assert response.data["title"] == update_data["title"]
    assert response.data["description"] == update_data["description"]

    book.refresh_from_db()
    assert book.title == update_data["title"]
    assert book.description == update_data["description"]


@pytest.mark.django_db
def test_delete_book(auth_client, book):
    url = reverse("book_detail", kwargs={"id": book.id})

    response = auth_client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert not Book.objects.filter(id=book.id).exists()


@pytest.mark.django_db
def test_rate_book(auth_client, book):
    url = reverse("rate_book", kwargs={"id": book.id})
    rating_data = {"rating": 4.5}

    response = auth_client.post(url, rating_data, format="json")

    assert response.status_code == status.HTTP_200_OK
    assert response.data["rating"] == rating_data["rating"]
    assert Rating.objects.count() == 1

    new_rating_data = {"rating": 3.5}
    response = auth_client.post(url, new_rating_data, format="json")

    assert response.status_code == status.HTTP_200_OK
    assert response.data["rating"] == new_rating_data["rating"]
    assert Rating.objects.count() == 1


@pytest.mark.django_db
def test_rate_nonexistent_book(auth_client):
    url = reverse("rate_book", kwargs={"id": 999})
    rating_data = {"rating": 4.5}

    response = auth_client.post(url, rating_data, format="json")

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "error" in response.data
    assert Rating.objects.count() == 0


@pytest.mark.django_db
def test_delete_genre(auth_client, genre):
    url = reverse("delete_genre", kwargs={"id": genre.id})

    response = auth_client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert not Genre.objects.filter(id=genre.id).exists()
