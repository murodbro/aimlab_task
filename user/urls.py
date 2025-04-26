from django.urls import path

from user.views import UserApiView, UserLoginApiView, UserSignupApiView

urlpatterns = [
    path("signup/", view=UserSignupApiView.as_view()),
    path("login/", view=UserLoginApiView.as_view()),
    path("me/", view=UserApiView.as_view()),
]
