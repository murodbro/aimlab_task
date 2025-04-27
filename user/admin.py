from django.contrib import admin

from user.models import User


class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = ("email", "name", "role", "is_staff", "is_active", "is_superuser")
    list_filter = ("email", "role", "is_active")

    search_fields = ("email",)
    ordering = ("email",)
    readonly_fields = ("password", "last_login", "created_at", "updated_at")


admin.site.register(User, UserAdmin)
