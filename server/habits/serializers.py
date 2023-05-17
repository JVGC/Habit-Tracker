from rest_framework import serializers
from .models import Habit

class HabitSerializer(serializers.ModelSerializer):
  completed = serializers.BooleanField(required=False)
  class Meta:
      model = Habit
      fields = ('id','name', 'start_at', 'completed')