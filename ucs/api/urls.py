from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path("auth/", include('auth.urls')),
    path("discussions/", include("discussions.urls")),
    path("users/", include("users.urls")),
]
