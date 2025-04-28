from django.urls import path

from user.views import UserApiView, UserLoginApiView, UserSignupApiView

urlpatterns = [
    path("signup/", view=UserSignupApiView.as_view(), name="signup"),
    path("login/", view=UserLoginApiView.as_view(), name="login"),
    path("me/", view=UserApiView.as_view(), name="profile"),
]
