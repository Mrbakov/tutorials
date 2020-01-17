# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import Special, Attendance, Date, Foodwish
from coosto_lunch.serializers import SpecialSerializer, AttendanceSerializer, DateSerializer, FoodwishSerializer
from rest_framework import viewsets

from .permissions import IsAdminOrReadOnly


class DateViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Date.objects.all()
    serializer_class = DateSerializer
    permission_classes = [IsAdminOrReadOnly]


class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [IsAdminOrReadOnly]


class SpecialViewSet(viewsets.ModelViewSet):
    queryset = Special.objects.all()
    serializer_class = SpecialSerializer
    permission_classes = [IsAdminOrReadOnly]


class FoodwishesViewSet(viewsets.ModelViewSet):
    queryset = Foodwish.objects.all()
    serializer_class = FoodwishSerializer
