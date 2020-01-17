# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Date(models.Model):
    date = models.DateField()

    def __str__(self):
        return self.date.strftime("%d-%m-%Y")


class Attendance(models.Model):
    attending = models.IntegerField()
    date = models.OneToOneField(Date, blank=True, on_delete=models.CASCADE)


class Special(models.Model):
    name = models.CharField(max_length=50)
    dates = models.ManyToManyField(Date, blank=True)

    def __str__(self):
        return self.name


class Foodwish(models.Model):
    food = models.TextField()
    approved = models.BooleanField()
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.food
