from todo_list.serializers.project import ProjectCreateSerializer, ProjectSerializer
from todo_list.models.project import Project
from rest_framework import generics
from rest_framework import permissions


class ProjectCreate(generics.CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        self_depth = 1
        if 'parent_project' in self.request.data.keys():
            parent_project = self.request.data['parent_project']
            parent_depth = Project.objects.get(pk=parent_project).depth
            self_depth = parent_depth + 1

        serializer.save(owner=self.request.user, depth=self_depth)


class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProjectsByOwnerId(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Project.objects.filter(owner=user, depth=1)
