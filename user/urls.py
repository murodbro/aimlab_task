from django.urls import path

from user.views import (
    UserApiView,
    UserLoginApiVIew,
    UserSignupApiVIew,
)

urlpatterns = [
    path("signup/", view=UserSignupApiVIew.as_view()),
    path("login/", view=UserLoginApiVIew.as_view()),
    path("me/", view=UserApiView.as_view()),
]
