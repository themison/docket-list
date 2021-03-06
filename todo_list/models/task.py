from django.db import models
from django.db.models.deletion import CASCADE


class Task(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=1000, blank=True)
    file = models.FileField(upload_to='uploads/', blank=True)
    project = models.ForeignKey(
        'Project', related_name='project_tasks', blank=False, on_delete=CASCADE)
    owner = models.ForeignKey('auth.User', blank=False, on_delete=CASCADE)
