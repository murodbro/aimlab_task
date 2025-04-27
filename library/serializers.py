from rest_framework import serializers

from library.models import Author, Book, Genre


class BookSerializer(serializers.ModelSerializer):
    genre = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = [
            "id",
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


class BookCreateSerializer(serializers.ModelSerializer):
    author = serializers.IntegerField()
    genre = serializers.IntegerField()
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

    def validate_author(self, value):
        if not Author.objects.filter(id=value).exists():
            raise serializers.ValidationError("Author not found.")
        return value

    def validate_genre(self, value):
        if not Genre.objects.filter(id=value).exists():
            raise serializers.ValidationError("Genre not found.")
        return value


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
