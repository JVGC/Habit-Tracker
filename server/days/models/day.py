""" Days Model """
from django.db import models

from habits.models.Habit import Habit


class Day(models.Model):
    """Day Model"""

    date = models.DateField()
    habits = models.ManyToManyField(Habit, through="DayHabit")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.date.isoformat()

    class Meta:
        """Day Model Meta Class"""

        db_table = "days"  # Change Table Name
