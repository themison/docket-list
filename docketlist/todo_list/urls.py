from todo_list.views.task import TaskSingle, TaskByProjectId, TaskCreate
from django.urls import path
from .views.project import ProjectDetail, ProjectCreate, ProjectsByOwnerId


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('project/get-by-user', ProjectsByOwnerId.as_view()),
    path('project/create-project/', ProjectCreate.as_view()),
    path('project/<int:pk>/', ProjectDetail.as_view()),
    path('task/create-task', TaskCreate.as_view()),
    path('task/<int:pk>', TaskSingle.as_view()),
    path('task/by-folder-id/<int:project>', TaskByProjectId.as_view()),

]
