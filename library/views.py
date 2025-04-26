from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from drf_spectacular.utils import extend_schema, extend_schema_view

from library.models import Author, Book, Genre
from library.serializers import AuthorCreateSerializer, BookCreateSerializer, BookResponseSerializer


@extend_schema(tags=["Author"])
class CreateListAuthorApiView(APIView):
    serializer_class = AuthorCreateSerializer

    def get(self, request):
        authors = Author.objects.all()
        serializer = self.serializer_class(authors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, reqeust):
        serializer = self.serializer_class(data=reqeust.data)
        serializer.is_valid(raise_exception=True)

        author = Author.objects.create(**serializer.validated_data)
        return Response(
            {
                "id": author.id,
                "first_name": author.first_name,
                "last_name": author.last_name,
                "birth_date": author.birth_date,
                "death_date": author.death_date,
            },
            status=status.HTTP_201_CREATED,
        )


@extend_schema(tags=["Author"])
@extend_schema_view(put=extend_schema(exclude=True))
class AuthorDetailApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = AuthorCreateSerializer
    queryset = Author.objects.all()
    lookup_field = "id"


@extend_schema(tags=["Book"])
class CreateBookApiView(APIView):
    serializer_class = BookCreateSerializer

    def post(self, request):
        data = request.data.copy()
        author_id = data.pop("author")
        genre_id = data.pop("genre")

        author = Author.objects.filter(id=author_id).first()
        if not author:
            return Response({"error": "Author not found"}, status=status.HTTP_400_BAD_REQUEST)

        genre = Genre.objects.filter(id=genre_id).first()
        if not genre:
            return Response({"error": "Genre not found"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)

        book = Book.objects.create(
            author=author,
            genre=genre,
            **serializer.validated_data,
        )

        return Response(BookResponseSerializer(book).data, status=status.HTTP_201_CREATED)


@extend_schema(tags=["Book"])
@extend_schema_view(put=extend_schema(exclude=True))
class BookDetailsApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = BookResponseSerializer
    queryset = Book.objects.all()
    lookup_field = "id"
