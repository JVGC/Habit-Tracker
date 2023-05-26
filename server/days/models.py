""" Days related Models """

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
