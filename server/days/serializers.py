""" Days App Serializers """
from rest_framework import serializers
from .models import Day, DayHabit


class DaySerializer(serializers.ModelSerializer):
    """Day Model Serializer"""

    completed = serializers.IntegerField(required=False)
    total = serializers.IntegerField(required=False)

    class Meta:
        model = Day
        fields = ("id", "date", "completed", "total")


class DayHabitSerializer(serializers.ModelSerializer):
    """DayHabit Model Serialzier"""

    class Meta:
        model = DayHabit
        fields = ("day", "habit", "completed")
