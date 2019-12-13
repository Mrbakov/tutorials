from django.db import models


# Create your models here.
class Week(models.Model):
    name = models.CharField(max_length=50)
    number = models.IntegerField()


class Day(models.Model):
    week = models.ForeignKey(Week, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    number = models.IntegerField()
