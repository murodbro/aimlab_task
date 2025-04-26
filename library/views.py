from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView, DestroyAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiParameter

from library.models import Author, Book, Genre, Rating
from library.serializers import (
    AuthorCreateSerializer,
    BookCreateSerializer,
    BookResponseSerializer,
    DeleteSerializer,
    RateBookSerializer,
)


# API to Create a new Author or List all Authors
@extend_schema(
    tags=["Author"],
    description="Create a new author or list all authors",
)
class CreateListAuthorApiView(APIView):
    serializer_class = AuthorCreateSerializer

    @extend_schema(
        operation_id="list_authors",
        description="Retrieve a list of all authors",
    )
    def get(self, request):
        authors = Author.objects.all()
        serializer = self.serializer_class(authors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(description="Create a new author")
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
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


# API to Retrieve, Update, or Delete a specific Author
@extend_schema(
    tags=["Author"],
    operation_id="retrieve_author",
    description="Retrieve, update or delete a specific author by ID",
)
@extend_schema_view(put=extend_schema(exclude=True))  # PUT method is hidden from Swagger
class AuthorDetailApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = AuthorCreateSerializer
    queryset = Author.objects.all()
    lookup_field = "id"


# API to Create a Book (with optional cover image)
@extend_schema(
    tags=["Book"],
    description="Create a new book with optional cover image upload",
    request={
        "multipart/form-data": BookCreateSerializer,
    },
    responses={201: BookResponseSerializer},
    parameters=[
        OpenApiParameter(
            name="cover",
            type=OpenApiTypes.BINARY,
            location="form",
            description="Book cover image file",
            required=False,
        ),
    ],
)
class CreateBookApiView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = BookCreateSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        author_id = serializer.validated_data.pop("author")
        genre_name = serializer.validated_data.pop("genre")

        author = Author.objects.filter(id=author_id).first()
        if not author:
            return Response({"error": "Author not found"}, status=status.HTTP_400_BAD_REQUEST)

        genre, _ = Genre.objects.get_or_create(name=genre_name)
        # if not genre:
        #     return Response({"error": "Genre not found"}, status=status.HTTP_400_BAD_REQUEST)

        book = Book.objects.create(
            author=author,
            genre=genre,
            **serializer.validated_data,
        )

        return Response(BookResponseSerializer(book).data, status=status.HTTP_201_CREATED)


# API to Retrieve, Update, or Delete a Book
@extend_schema(
    tags=["Book"],
    description="Retrieve, update, or delete a specific book by ID",
)
@extend_schema_view(put=extend_schema(exclude=True))
class BookDetailsApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = BookResponseSerializer
    queryset = Book.objects.all()
    lookup_field = "id"


# API to Rate a Book
@extend_schema(
    tags=["Book"],
    description="Rate a specific book. Book ID is needed in the URL path.",
)
class RateBookApiView(APIView):
    serializer_class = RateBookSerializer

    def post(self, request, id):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        book = Book.objects.filter(id=id).first()
        if not book:
            return Response({"error": "Book not found"}, status=status.HTTP_400_BAD_REQUEST)

        rate, created = Rating.objects.get_or_create(
            user=request.user,
            book=book,
            defaults={"rating": serializer.validated_data.get("rating")},
        )
        if not created:
            rate.rating = serializer.validated_data.get("rating")
            rate.save()

        return Response(
            {
                "user": request.user.id,
                "book": book.id,
                "rating": rate.rating,
            },
            status=status.HTTP_200_OK,
        )


# API to Delete a Genre
@extend_schema(
    tags=["Book"],
    description="Delete a genre by ID",
)
class DeleteGenreApiView(DestroyAPIView):
    serializer_class = DeleteSerializer
    queryset = Genre.objects.all()
    lookup_field = "id"
