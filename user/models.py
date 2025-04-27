import uuid
from django.db.models import CharField, EmailField, BooleanField
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from configs.models import BaseModel
from user.manager import Role, UserManager


class User(BaseModel, AbstractBaseUser, PermissionsMixin):
    id = CharField(primary_key=True, default=uuid.uuid4, editable=False, max_length=36)
    name = CharField(max_length=255)
    email = EmailField(unique=True)
    role = CharField(choices=Role.choices, default=Role.USER)

    is_active = BooleanField(default=True)
    is_staff = BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def __str__(self):
        return self.name
