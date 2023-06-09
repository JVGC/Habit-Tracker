""" Day Habit Models """

from django.db import models

from habits.models.habit import Habit
from .day import Day


class DayHabit(models.Model):
    """DayHabit Model"""

    completed = models.BooleanField(default=False)
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    day = models.ForeignKey(Day, on_delete=models.CASCADE)

    class Meta:
        """DayHabit Model Meta Class"""

        unique_together = ["habit", "day"]

    def __str__(self) -> str:
        return f"{self.day.date.isoformat()} - {self.habit.name}"
