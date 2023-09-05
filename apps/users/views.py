from django.utils.translation import gettext_lazy as _
from rest_framework import status
from rest_framework.authentication import get_authorization_header
from rest_framework.generics import RetrieveAPIView, CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User, BlacklistedToken
from .serializers import UserModelSerializer, LogoutSerializer


# Create your views here.
class MeView(RetrieveAPIView):
    """Display profile for current user"""

    def get(self, request, *args, **kwargs):
        queryset = User.objects.get(pk=request.user.pk)
        serializer = self.get_serializer(queryset, many=False)
        return Response(serializer.data)

    serializer_class = UserModelSerializer


class LogoutView(CreateAPIView):
    """Just acknowledge the API is up and running"""

    serializer_class = LogoutSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        auth = get_authorization_header(request).split()
        if serializer.is_valid():
            for token in [serializer.data.get('refresh_token'), auth[-1].decode()]:  # auth[-1] is access_token
                BlacklistedToken.objects.get_or_create(token=token, user=request.user)
            return Response({})
        return Response({"error": _("Incorrect data")}, status=status.HTTP_400_BAD_REQUEST)


class CheckView(APIView):
    """Just acknowledge the API is up and running"""

    permission_classes = [AllowAny]

    def get(self, request, format=None):
        return Response("OK")
