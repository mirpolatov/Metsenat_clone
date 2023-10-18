from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from root import settings

schema_view = get_schema_view(
    openapi.Info(
        title="Metsenat API",
        default_version='v1',
        description="",
        terms_of_service="https://www.instagram.com/mirpolatov_m/",
        contact=openapi.Contact(email="mirazizmirpolatov9@gmail.com"),
        license=openapi.License(name="@mirpolatov_m"),
    ),
    public=True,
    permission_classes=[AllowAny],
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('apps.urls')),

]

if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),
        path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    ]
