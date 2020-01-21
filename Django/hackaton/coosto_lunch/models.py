# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Overview(models.Model):
    date = models.DateField()

    def __str__(self):
        return self.date.strftime("%d-%m-%Y")


class Role(models.Model):
    ROLE_CHOICES = (
        ('ADMIN', 'Admin'),
        ('USER', 'User'),
    )
    role = models.CharField(choices=ROLE_CHOICES, default='USER', max_length=20)

    def __str__(self):
        return self.role


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=60)
    role = models.OneToOneField(
        Role,
        on_delete=models.CASCADE,
        primary_key=True,
        default='USER'
    )
    overviews = models.ManyToManyField(Overview, blank=True)

    def __str__(self):
        return self.email


class Special(models.Model):
    name = models.CharField(max_length=50)
    overviews = models.ManyToManyField(Overview, blank=True)

    def __str__(self):
        return self.name
