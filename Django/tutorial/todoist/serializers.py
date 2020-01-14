from django.contrib.auth.models import User
from rest_framework import serializers

from todoist.models import Task, Project


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'project', 'owner']


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    def validate_title(self, title):
        if 'project' not in title.lower():
            raise serializers.ValidationError('The project title must contain the word project.')
        return title

    class Meta:
        model = Project
        fields = ['id', 'title', 'owner']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    tasks = serializers.HyperlinkedRelatedField(many=True, view_name='task-detail', read_only=True)
    projects = serializers.HyperlinkedRelatedField(many=True, view_name='project-detail', read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'tasks', 'projects']
