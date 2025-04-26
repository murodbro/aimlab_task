from rest_framework import serializers

from library.models import Author, Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class BookCreateSerializer(serializers.ModelSerializer):
    author = serializers.IntegerField()
    genre = serializers.CharField()
    cover = serializers.ImageField(required=False)

    class Meta:
        model = Book
        fields = [
            "author",
            "genre",
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


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = [
            "id",
            "first_name",
            "last_name",
            "birth_date",
            "death_date",
        ]


class BookResponseSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    genre = serializers.SerializerMethodField()

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

    def get_genre(self, obj):
        if obj.genre:
            return obj.genre.name
        return None


class RateBookSerializer(serializers.Serializer):
    rating = serializers.FloatField()


class DeleteSerializer(serializers.Serializer):
    pass
