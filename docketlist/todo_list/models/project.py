from django.db import models
from django.db.models.deletion import CASCADE


class Project(models.Model):
    title = models.CharField(max_length=100, blank=False)
    color = models.CharField(max_length=15, blank=True, default='')
    parent_project = models.ForeignKey(
        'self', blank=True, on_delete=CASCADE, null=True)
    owner = models.ForeignKey('auth.User', blank=False, on_delete=CASCADE)
    depth = models.PositiveSmallIntegerField(blank=False, default=1)
