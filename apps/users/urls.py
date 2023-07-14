from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from . import views
from djoser import views as djoser_views

urlpatterns = [
    path("me/", views.MeView.as_view(), name="me"),
    path("test/mailhog/", views.MailhogTestView.as_view(), name="mailhog_test"),
    path('api/tokens/generate/', jwt_views.TokenObtainPairView.as_view(), name='tokens_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', jwt_views.TokenVerifyView.as_view(), name='token_verify'),
]
