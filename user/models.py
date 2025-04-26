import uuid
from django.db.models import CharField, EmailField, TextChoices
from django.contrib.auth.models import AbstractBaseUser

from user.manager import UserManager


class Role(TextChoices):
    USER = "user", "User"
    ADMIN = "admin", "Admin"


class User(AbstractBaseUser):
    id = CharField(primary_key=True, default=uuid.uuid4, editable=False, max_length=36)
    name = CharField(max_length=255)
    email = EmailField(unique=True)
    role = CharField(choices=Role.choices, default=Role.USER)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def __str__(self):
        return self.name
