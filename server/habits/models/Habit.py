""" Habits Model """
from django.db import models


class Habit(models.Model):
    """Habit Model"""

    name = models.CharField(max_length=30)
    start_at = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.name)

    class Meta:
        db_table = "habits"  # Change Table Name

    @staticmethod
    def get_habits_by_date(date):
        """Get all the habits where start_at are less or equal then a given date"""
        return Habit.objects.filter(start_at__lte=date).order_by("start_at")
