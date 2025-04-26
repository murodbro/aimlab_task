from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_spectacular.utils import extend_schema

from user.models import User
from user.serializers import UserLoginSerializer, UserSerializer, UserSignupSerializer


@extend_schema(tags=["User"])
class UserSignupApiVIew(APIView):
    serializer_class = UserSignupSerializer
    permission_classes = []
    authentication_classes = []

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                "status": "success",
                "user": {
                    "id": serializer.instance.id,
                    "name": serializer.instance.name,
                    "email": serializer.instance.email,
                    "password_set": True,
                },
            },
            status=status.HTTP_201_CREATED,
        )


@extend_schema(tags=["User"])
class UserLoginApiVIew(APIView):
    serializer_class = UserLoginSerializer
    permission_classes = []
    authentication_classes = []

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        if not email or not password:
            return Response({"error": "Email and password required."}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.filter(email=email).first()
        if not user:
            return Response({"error": "User not found"}, status=status.HTTP_400_BAD_REQUEST)

        if not user.check_password(password):
            return Response(
                {
                    "field_errors": {
                        "email": "Incorrect credentials",
                        "password": "Incorrect credentials",
                    },
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        refresh = RefreshToken.for_user(user)

        return Response(
            {"refresh": str(refresh), "access": str(refresh.access_token)},
            status=status.HTTP_200_OK,
        )


@extend_schema(tags=["User"])
class UserApiView(APIView):
    serializer_class = UserSerializer

    def get(self, request):
        user = User.objects.filter(id=request.user.id).first()
        serializer = self.serializer_class(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


@extend_schema(
    tags=["Authentication JWT tokens"],
    description="Obtain a pair of access and refresh tokens.",
)
class CustomTokenObtainPairView(TokenObtainPairView):
    pass


@extend_schema(
    tags=["Authentication JWT tokens"],
    description="Refresh an access token using a refresh token.",
)
class CustomTokenRefreshView(TokenRefreshView):
    pass
