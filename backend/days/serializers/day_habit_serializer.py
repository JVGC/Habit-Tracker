""" Day Habit Serializer """
from rest_framework import serializers
from days.models import DayHabit


class DayHabitSerializer(serializers.ModelSerializer):
    """DayHabit Model Serialzier"""

    class Meta:
        model = DayHabit
        fields = ("day", "habit", "completed")
