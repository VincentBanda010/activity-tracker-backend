# activities/data/models.py

from django.db import models
from django.contrib.auth.models import User

class ActivityModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities', null=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
