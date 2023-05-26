"""Day Model Serializer"""

from rest_framework import serializers
from days.models import Day


class DaySerializer(serializers.ModelSerializer):
    """Day Model Serializer"""

    completed = serializers.IntegerField(required=False)
    total = serializers.IntegerField(required=False)

    class Meta:
        model = Day
        fields = ("id", "date", "completed", "total")
