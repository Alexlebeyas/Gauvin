from rest_framework.generics import RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.core.mail import send_mail

from .serializers import UserModelSerializer
from .models import User

# Create your views here.
class MeView(RetrieveAPIView):
    """Display profile for current user"""
    def get(self, request, *args, **kwargs):
        queryset = User.objects.get(pk=request.user.pk)
        serializer = self.get_serializer(queryset, many=False)
        return Response(serializer.data)
    serializer_class = UserModelSerializer


class MailhogTestView(RetrieveAPIView):
    """Remove this view before produdction deployement. This was to confirm email functio"""
    def get(self, request, *args, **kwargs):
        queryset = User.objects.get(pk=request.user.pk)
        serializer = self.get_serializer(queryset, many=False)
        send_mail(
            "Subject here",
            "Here is the message.",
            f"{queryset.email}",
            ["to@example.com"],
            fail_silently=False,
        )
        return Response(serializer.data)
    serializer_class = UserModelSerializer

class CheckView(APIView):
    """Just acknowledge the API is up and running"""
    permission_classes = [AllowAny]
    def get(self, request, format=None):
        return Response("OK")