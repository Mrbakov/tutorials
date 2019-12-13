from django.contrib.auth.models import User, Group
from rest_framework import serializers, generics
from .models import Week, Day


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class WeekSerializer(generics.ListAPIView):
    class Meta:
        model = Week
        fields = ['name', 'number']


class DaySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Day
        fields = ['week', 'name', 'number']
