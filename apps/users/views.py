from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from .serializers import UserModelSerializer
from rest_framework.permissions import IsAuthenticated
from .models import User
from django.core.mail import send_mail


# Create your views here.
class MeView(ListAPIView):
    """Display profile for current user"""
    def list(self, request, *args, **kwargs):
        queryset = User.objects.get(pk=request.user.pk)
        serializer = self.get_serializer(queryset, many=False)
        return Response(serializer.data)
    serializer_class = UserModelSerializer


class MailhogTestView(ListAPIView):
    """Display profile for current user"""
    def list(self, request, *args, **kwargs):
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