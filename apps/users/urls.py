from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from . import views

urlpatterns = [
    path("users/me/", views.MeView.as_view(), name="me"),
    path("test/mailhog/", views.MailhogTestView.as_view(), name="mailhog_test"),
    path('token/generate/', jwt_views.TokenObtainPairView.as_view(), name='tokens_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', jwt_views.TokenVerifyView.as_view(), name='token_verify'),
    path('users/check/', views.CheckView.as_view(), name="sanity_check"),
]
