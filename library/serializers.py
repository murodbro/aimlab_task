from rest_framework import serializers

from library.models import Author, Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class BookCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            "title",
            "description",
            "length",
            "published_date",
            "created_date",
            "copies_sold",
            "price",
            "discount",
            "cover",
        ]


class AuthorCreateSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = [
            "id",
            "first_name",
            "last_name",
            "birth_date",
            "death_date",
            "books",
        ]
        extra_kwargs = {"id": {"read_only": True}}


class BookResponseSerializer(serializers.ModelSerializer):
    author = AuthorCreateSerializer()
    genre = serializers.CharField(source="genre.name")

    class Meta:
        model = Book
        fields = [
            "id",
            "author",
            "title",
            "description",
            "genre",
            "length",
            "published_date",
            "created_date",
            "copies_sold",
            "price",
            "discount",
            "cover",
        ]
