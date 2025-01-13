# activities/data/serializers.py

from rest_framework import serializers
from .models import ActivityModel

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityModel
        fields = ['id', 'title', 'description', 'date', 'created_at']
        read_only_fields = ['id', 'date', 'created_at']
    
    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError("Title cannot be empty.")
        return value

    def validate_description(self, value):
        if not value.strip():
            raise serializers.ValidationError("Description cannot be empty.")
        return value
