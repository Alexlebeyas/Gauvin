from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from . import views

urlpatterns = [
    path("users/me/", views.MeView.as_view(), name="me"),
    path("tokens/generate/", jwt_views.TokenObtainPairView.as_view(), name="token_get"),
    path("tokens/refresh/", jwt_views.TokenRefreshView.as_view(), name="token_refresh"),
    path("tokens/logout/", views.LogoutView.as_view(), name="logout"),
]
