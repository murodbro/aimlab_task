from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_spectacular.utils import extend_schema

from user.models import User
from user.serializers import (
    UserLoginSerializer,
    UserSerializer,
    UserSignupSerializer,
)


# API to Sign up (Register) a new User
@extend_schema(
    tags=["User"],
    description="Sign up a new user with name, email, and password.",
)
class UserSignupApiView(APIView):
    serializer_class = UserSignupSerializer
    permission_classes = []  # Open to unauthenticated users
    authentication_classes = []

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        response_data = {
            "status": "success",
            "data": {
                "user": {
                    "id": user.id,
                    "name": user.name,
                    "email": user.email,
                }
            },
        }
        return Response(response_data, status=status.HTTP_201_CREATED)


# API to Login a User
@extend_schema(
    tags=["User"],
    description="Log in an existing user and obtain JWT tokens.",
)
class UserLoginApiView(APIView):
    serializer_class = UserLoginSerializer
    permission_classes = []
    authentication_classes = []

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        refresh = RefreshToken.for_user(serializer.user)

        return Response(
            {"refresh": str(refresh), "access": str(refresh.access_token)},
            status=status.HTTP_200_OK,
        )


# API to Get current User profile
@extend_schema(
    tags=["User"],
    description="Retrieve the profile information of the currently authenticated user.",
)
class UserApiView(APIView):
    serializer_class = UserSerializer

    def get(self, request):
        user = User.objects.filter(id=request.user.id).first()
        serializer = self.serializer_class(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


# API to Obtain Access and Refresh tokens (login)
@extend_schema(
    tags=["Authentication JWT tokens"],
    description="Obtain a pair of access and refresh tokens.",
)
class CustomTokenObtainPairView(TokenObtainPairView):
    pass


# API to Refresh Access Token
@extend_schema(
    tags=["Authentication JWT tokens"],
    description="Refresh an access token using a refresh token.",
)
class CustomTokenRefreshView(TokenRefreshView):
    pass
