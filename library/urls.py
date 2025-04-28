from django.urls import path

from library.views import (
    AuthorDetailApiView,
    BookDetailsApiView,
    CreateBookApiView,
    CreateListAuthorApiView,
    DeleteGenreApiView,
    RateBookApiView,
)


urlpatterns = [
    path("authors/", view=CreateListAuthorApiView.as_view(), name="create_author"),
    path("books/", view=CreateBookApiView.as_view(), name="create_book"),
    path("authors/<int:id>/", view=AuthorDetailApiView.as_view(), name="author_detail"),
    path("books/<int:id>/", view=BookDetailsApiView.as_view(), name="book_detail"),
    path("genres/<int:id>/", view=DeleteGenreApiView.as_view(), name="delete_genre"),
    path("books/<int:id>/rate/", view=RateBookApiView.as_view(), name="rate_book"),
]
