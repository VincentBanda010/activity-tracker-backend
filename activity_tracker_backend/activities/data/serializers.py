# activities/data/serializers.py

from rest_framework import serializers
from .models import ActivityModel

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityModel
        fields = ['id', 'user', 'title', 'description', 'date', 'created_at']
        read_only_fields = ['id', 'user', 'date', 'created_at']
