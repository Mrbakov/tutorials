from .models import Attendance, Special, Date, Foodwish
from rest_framework import serializers


class DateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Date
        fields = ['date']


class AttendanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Attendance
        fields = ['attending', 'date']


class SpecialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Special
        fields = ['name', 'dates']


class FoodwishSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Foodwish
        fields = ['food', 'approved', 'score']
