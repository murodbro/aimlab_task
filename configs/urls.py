from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

from user.views import CustomTokenObtainPairView, CustomTokenRefreshView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("user/", include("user.urls")),
    path("library/", include("library.urls")),
]


urlpatterns += [
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("schema/swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger"),
    path("schema/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    path("token/", view=CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", view=CustomTokenRefreshView.as_view(), name="token_refresh"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
