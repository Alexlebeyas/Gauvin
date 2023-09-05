import json

from apps.users.models import BlacklistedToken
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication


class LogoutVerifyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        """
        If the token exists in the header, we check that it is not blacklisted (logout).
        If this is the case we return a response 'Token is logout' otherwise we let the request pass.
        The login endpoint ('token_get') does not need this check. For the refresh of the token,
        we also want to make sure that the token sent in the body is not blacklisted
        :param request:
        :return:
        """
        raw_token = None
        if reverse('token_get') != request.META.get('PATH_INFO'):
            if reverse('token_refresh') == request.META.get('PATH_INFO'):
                body = json.loads(request.body.decode("utf-8"))
                raw_token = body.get('refresh')
            else:
                auth = JWTAuthentication()
                header = auth.get_header(request)
                raw_token = auth.get_raw_token(header).decode("utf-8") if header else None

        response = self.get_response(request)
        return self.render_response(response, raw_token)

    def render_response(self, response, raw_token):
        """
        If the token is blacklisted, we return the response "Token is logout"
        with a 403 status, otherwise we let the request pass
        :param response:
        :param raw_token:
        :return:
        """
        if raw_token and BlacklistedToken.objects.filter(token=raw_token).exists():
            response = Response(
                data={"detail": _("Token is logout"), },
                status=status.HTTP_403_FORBIDDEN
            )
            response.accepted_renderer = JSONRenderer()
            response.accepted_media_type = "application/json"
            response.renderer_context = {}
            response.render()

        return response
