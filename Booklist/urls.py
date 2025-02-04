
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import TokenBlacklistView

...

schema_view = get_schema_view(
   openapi.Info(
      title="World Readers API",
      default_version='v1',
      description="A glossary of book recommendations from readers near and far",
      terms_of_service="",
      contact=openapi.Contact(email="doobam007@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('wrv1-admin/', admin.site.urls),
    path('world-readers/v1/auth/', include('djoser.urls.jwt')),
    path('world-readers/v1/auth/', include('djoser.urls.authtoken')),
    path('world-readers/v1/auth/blacklist/', TokenBlacklistView.as_view()),
    path('world-readers/v1/', include('booklistAPI.urls')),
    path('world-readers/v1/signup/', include('authapp.urls')),
    path('world-readers/v1/doc<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('world-readers/v1/doc/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('world-readers/v1/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
