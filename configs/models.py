from django.db.models import Model, DateTimeField


class BaseModel(Model):
    class Meta:
        abstract = True

    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
