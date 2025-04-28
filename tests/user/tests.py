import pytest

from django.urls import reverse
from rest_framework import status


# Test Signup API
@pytest.mark.django_db
def test_user_signup(api_client):
    url = reverse("signup")

    payload = {
        "name": "Test User",
        "email": "user@example.com",
        "password": "Password123",
    }

    response = api_client.post(url, payload, format="json")

    assert response.status_code == status.HTTP_201_CREATED
    assert response.data["status"] == "success"
    assert response.data["data"]["user"]["email"] == payload["email"]


# Test Login API
@pytest.mark.django_db
def test_user_login(api_client, create_user):
    user = create_user(
        name="Test User",
        email="user@example.com",
        password="Password123",
    )

    url = reverse("login")

    payload = {"email": user.email, "password": "Password123"}

    response = api_client.post(url, payload, format="json")

    assert response.status_code == status.HTTP_200_OK
    assert "access" in response.data
    assert "refresh" in response.data


# Test Get User Profile API
@pytest.mark.django_db
def test_user_profile(api_client, create_user):
    user = create_user(
        name="Test User",
        email="user@example.com",
        password="Password123",
    )

    api_client.force_authenticate(user=user)

    url = reverse("profile")
    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response.data["email"] == user.email
