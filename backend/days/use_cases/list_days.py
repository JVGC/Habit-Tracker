""" List Days Use Case Class """

from rest_framework.exceptions import ReturnDict

from days.serializers import DaySerializer
from days.models.day import Day
from habits.models import Habit


class ListDaysUseCase:
    """List Days Use Case Implementation"""

    @staticmethod
    def _get_days_with_completed_habits_count():
        """Return a List of Days with the amount of completed habits for each one ordered by Date"""
        return (
            Day.objects.all()
            .annotate(completed=Day.count_completed_habits())
            .order_by("date")
        )

    @staticmethod
    def execute() -> ReturnDict:
        """Return all Days ordered by date ascendent,
        and for each day, returns the number of completed habits
        and the total amount of habits to be completed.
        """
        days = ListDaysUseCase._get_days_with_completed_habits_count()

        day_serializer = DaySerializer(days, many=True)
        for day in day_serializer.data:
            day["total"] = len(Habit.get_habits_by_date(day["date"]))

        return day_serializer.data
