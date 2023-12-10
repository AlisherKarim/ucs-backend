from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views

from . import views

urlpatterns = [
    path("", views.UserListView.as_view(), name="user list view")
]
