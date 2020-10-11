from rest_framework import serializers
from api.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password', 'name', 'cellphone')


class FullSerializer(serializers.ModelSerializer):
    class Meta:
        model = Full
        fields = '__all__'


class EditedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Edited
        fields = '__all__'
