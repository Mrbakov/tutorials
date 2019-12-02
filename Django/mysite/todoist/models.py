from django.db import models


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=50)
    favorite = models.BooleanField(default=False)


class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    task_text = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completed_at = models.DateTimeField()
