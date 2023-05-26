""" List Days Use Case Class """

from typing import TypedDict
from django.db.models import Q, Count

from days.serializers import DaySerializer
from days.models.day import Day
from habits.models import Habit

ResponseData = TypedDict("response_data", {"status": int, "data": dict[str, str]})


class ListDaysUseCase:
    """List Days Use Case Implementation"""

    def execute(self) -> ResponseData:
        """Return all Days ordered by date ascendent,
        and for each day, returns the number of completed habits
        and the total amount of habits to be completed.
        """
        days = (
            Day.objects.all()
            .annotate(completed=Count("dayhabit", filter=Q(dayhabit__completed=True)))
            .order_by("date")
        )

        day_serializer = DaySerializer(days, many=True)
        for day in day_serializer.data:
            day["total"] = len(Habit.get_habits_by_date(day["date"]))
        return ResponseData(status=200, data=day_serializer.data)
