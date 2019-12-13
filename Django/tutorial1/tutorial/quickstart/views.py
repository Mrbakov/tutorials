from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from .models import Week, Day
from rest_framework import viewsets
from rest_framework import generics
from tutorial.quickstart.serializers import UserSerializer, GroupSerializer, WeekSerializer, DaySerializer


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows user groups to be viewed or edited.
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class WeekViewSet(generics.ListAPIView):
    queryset = Week.objects.all()
    serializer_class = WeekSerializer


class DayViewSet(generics.ListAPIView):
    queryset = Day.objects.all()
    serializer_class = DaySerializer


def test(request):
    return HttpResponse("This is a test")
