""" Habits App Serializers """
from rest_framework import serializers
from .models import Habit


class HabitSerializer(serializers.ModelSerializer):
    """Habit Model Serializer"""

    completed = serializers.BooleanField(required=False)

    class Meta:
        model = Habit
        fields = ("id", "name", "start_at", "completed")
