from rest_framework import serializers
# from .models import User
from .models import Tblcontactsecondaire as User


class UserModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('cemail',)
