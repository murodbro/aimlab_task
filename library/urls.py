from django.urls import path

from library.views import (
    AuthorDetailApiView,
    BookDetailsApiView,
    CreateBookApiView,
    CreateListAuthorApiView,
)


urlpatterns = [
    path("authors/", view=CreateListAuthorApiView.as_view()),
    path("books/", view=CreateBookApiView.as_view()),
    path("authors/<int:id>/", view=AuthorDetailApiView.as_view()),
    path("books/<int:id>/", view=BookDetailsApiView.as_view()),
]
