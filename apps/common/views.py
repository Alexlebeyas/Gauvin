from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


class CheckView(APIView):
    """Just acknowledge the API is up and running"""

    permission_classes = [AllowAny]

    def get(self, request, format=None):
        return Response("OK")
