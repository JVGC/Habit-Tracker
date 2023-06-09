""" Days Model """
from django.db import models
from django.db.models import Q, Count

from habits.models.habit import Habit


class Day(models.Model):
    """Day Model"""

    date = models.DateField()
    habits = models.ManyToManyField(Habit, through="DayHabit")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.date.isoformat()

    @staticmethod
    def get_by_date(date: str):
        """Get Day by its date. Should be in DD/MM/YYYY format."""
        return Day.objects.get(date=date)

    @staticmethod
    def count_completed_habits():
        """Annotate Helper function.
        Counts the number of completed habits in a Day."""
        return Count("dayhabit", filter=Q(dayhabit__completed=True))

    class Meta:
        """Day Model Meta Class"""

        db_table = "days"  # Change Table Name
