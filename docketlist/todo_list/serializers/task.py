from rest_framework import serializers
from todo_list.models import Task
from todo_list.models.task import Task


class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Task
        fields = '__all__'
