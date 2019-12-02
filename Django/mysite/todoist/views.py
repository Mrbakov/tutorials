from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseForbidden


def index(request):
    return HttpResponseForbidden("This page is forbidden")
