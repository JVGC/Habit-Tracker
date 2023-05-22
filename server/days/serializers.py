from rest_framework import serializers
from .models import Day


class DaySerializer(serializers.ModelSerializer):
    completed = serializers.IntegerField(required=False)
    total = serializers.IntegerField(required=False)

    class Meta:
        model = Day
        fields = ("id", "date", "completed", "total")
