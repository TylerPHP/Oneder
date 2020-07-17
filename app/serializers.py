from app.models import Clock
from rest_framework import serializers


class ClockSerializer(serializers.ModelSerializer):
    """Serializing alarm data"""
    class Meta:
        model = Clock
        fields = ("id", "time", "description")

