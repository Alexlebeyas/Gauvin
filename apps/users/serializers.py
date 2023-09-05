from rest_framework import serializers

from .models import User, BlacklistedToken


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email',)


class LogoutSerializer(serializers.Serializer):
    refresh_token = serializers.CharField(max_length=500, min_length=None, allow_blank=False, trim_whitespace=True)
