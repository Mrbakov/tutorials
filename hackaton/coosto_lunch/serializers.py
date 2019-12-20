from .models import User, Role, Overview, Special
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'role', 'overviews']


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['role']


class OverviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Overview
        fields = ['date']


class SpecialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Special
        fields = ['name', 'overviews']
