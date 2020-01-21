# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import User, Role, Special, Overview
from coosto_lunch.serializers import SpecialSerializer, UserSerializer, RoleSerializer, OverviewSerializer
# from django.http import Http404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
from rest_framework import generics


# Create your views here.
# class SpecialList(APIView):
#     """
#     List all specials or create a new one.
#     """
#
#     def get(self, request, format=None):
#         specials = Special.objects.all()
#         serializer = SpecialSerializer(specials, many=True)
#         return Response(serializer.data)
#
#     def post(self, reqest, format=None):
#         serializer = SpecialSerializer(data=reqest.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class SpecialDetail(APIView):
#     """
#     Retrieve, update or delete a special instance.
#     """
#
#     def get_object(self, pk):
#         try:
#             return Special.objects.get(pk=pk)
#         except Special.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, format=None):
#         special = self.get_object(pk)
#         serializer = SpecialSerializer(special)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         special = self.get_object(pk)
#         serializer = SpecialSerializer(special, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         special = self.get_object(pk)
#         special.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class SpecialList(generics.ListCreateAPIView):
    queryset = Special.objects.all()
    serializer_class = SpecialSerializer


class SpecialDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Special.objects.all()
    serializer_class = SpecialSerializer


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RoleList(generics.ListAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class OverViewList(generics.ListAPIView):
    queryset = Overview.objects.all()
    serializer_class = OverviewSerializer
