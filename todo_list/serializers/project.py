from todo_list.serializers.task import TaskSerializer
from todo_list.models.task import Task
from todo_list.models.project import Project
from rest_framework import serializers


class ProjectCreateSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Project
        fields = ['title', 'id', 'parent_project', 'owner', 'color', 'depth']


class ProjectSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    project_tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ['title', 'id', 'parent_project',
                  'owner', 'color', 'project_tasks']

    def get_fields(self):
        fields = super(ProjectSerializer, self).get_fields()
        fields['parent_project'] = ProjectSerializer()
        return fields
