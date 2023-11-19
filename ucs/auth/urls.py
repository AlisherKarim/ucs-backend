from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from . import views

urlpatterns = [
    path("login", views.MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("login/refresh", jwt_views.TokenRefreshView.as_view(), name="token_refresh"),
    path("signup", views.signup),
]
