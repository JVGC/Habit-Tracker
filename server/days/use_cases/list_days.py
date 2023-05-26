""" List Days Use Case Class """

from typing import TypedDict

from days.serializers import DaySerializer
from days.models.day import Day
from habits.models import Habit

ResponseData = TypedDict("response_data", {"status": int, "data": dict[str, str]})


class ListDaysUseCase:
    """List Days Use Case Implementation"""

    def _get_days_with_completed_habits_count(self):
        return (
            Day.objects.all()
            .annotate(completed=Day.count_completed_habits())
            .order_by("date")
        )

    def execute(self) -> ResponseData:
        """Return all Days ordered by date ascendent,
        and for each day, returns the number of completed habits
        and the total amount of habits to be completed.
        """
        days = self._get_days_with_completed_habits_count()

        day_serializer = DaySerializer(days, many=True)
        for day in day_serializer.data:
            day["total"] = len(Habit.get_habits_by_date(day["date"]))

        return ResponseData(status=200, data=day_serializer.data)
