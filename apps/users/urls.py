from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from . import views

urlpatterns = [
    path("users/me/", views.MeView.as_view(), name="me"),
    path("test/mailhog/", views.MailhogTestView.as_view(), name="mailhog_test"),
    path("tokens/generate/", jwt_views.TokenObtainPairView.as_view(), name="token_get"),
    path("tokens/refresh/", jwt_views.TokenRefreshView.as_view(), name="token_refresh"),
]
