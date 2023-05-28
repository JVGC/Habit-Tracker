""" Check Habit in a Day Use Case Class """
from typing import TypedDict
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist

from days.models import Day, DayHabit
from days.serializers import DayHabitSerializer
from habits.models import Habit
from habits.errors import HabitDoesNotExistError, HabitDidNotStartedYet


RequestData = TypedDict("request_data", {"habit": str, "date": str})
ResponseData = TypedDict("response_data", {"data": dict[str, str]})

DATE_FIELD_FORMAT = "%Y-%m-%d"


class CheckDayHabitUseCase:
    """Check Habit Use Case Implementation"""

    def _validate_input(self, data: RequestData) -> Habit:
        try:
            habit = Habit.get_by_id(data["habit"])
        except ObjectDoesNotExist as exc:
            raise HabitDoesNotExistError() from exc

        if not habit.has_started(
            datetime.strptime(data["date"], DATE_FIELD_FORMAT).date()
        ):
            raise HabitDidNotStartedYet()

        return habit

    def execute(self, data: RequestData) -> ResponseData:
        """Marks an habit in a given date as completed if it's completed
        and as not completed if it's already completed.
        """
        habit = self._validate_input(data)

        try:
            day = Day.get_by_date(data["date"])
        except ObjectDoesNotExist:
            day = Day(date=data["date"])
            day.save()

        day_habit: DayHabit
        try:
            day_habit = DayHabit.objects.get(habit=habit, day=day)
            day_habit.completed = not day_habit.completed
            day_habit.save(force_update=True)
        except ObjectDoesNotExist:
            day_habit = DayHabit(habit=habit, day=day, completed=True)
            day_habit.save()

        serializer = DayHabitSerializer(day_habit)
        return ResponseData(data=serializer.data)
