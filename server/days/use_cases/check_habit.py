""" Check Habit in a Day Use Case Class """
from typing import TypedDict, Optional, Any
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist

from days.models import Day, DayHabit
from days.serializers import DaySerializer, DayHabitSerializer
from habits.models import Habit


RequestData = TypedDict("request_data", {"habit": str, "date": str})
ResponseData = TypedDict("response_data", {"status": int, "data": dict[str, str]})
IsValidResponse = TypedDict("is_valid_response", {"is_valid": bool, "data": Any})

DATE_FIELD_FORMAT = "%Y-%m-%d"


class CheckHabitUseCase:
    """Check Habit Use Case Implementation"""

    def _validate_input(self, data: RequestData) -> IsValidResponse:
        day_serializer = DaySerializer(data={"date": data["date"]})  # type: ignore
        is_date_valid = day_serializer.is_valid()
        if not is_date_valid:
            return IsValidResponse(
                is_valid=False,
                data={"status": 400, "data": day_serializer.errors},
            )
        return IsValidResponse(is_valid=True, data=None)

    def _validate_habit(self, data: RequestData) -> IsValidResponse:
        try:
            habit = Habit.get_by_id(data["habit"])
        except ObjectDoesNotExist:
            return IsValidResponse(
                is_valid=False,
                data={"status": 404, "data": {"habit": "Habit does not exist"}},
            )
        if not habit.has_started(
            datetime.strptime(data["date"], DATE_FIELD_FORMAT).date()
        ):
            return IsValidResponse(
                is_valid=False,
                data={"status": 400, "data": {"date": "This habit didn't start yet"}},
            )
        return IsValidResponse(is_valid=True, data=habit)

    def execute(self, data: RequestData) -> ResponseData:
        """Marks an habit in a given date as completed if it's completed
        and as not completed if it's already completed.
        """
        is_input_valid = self._validate_input(data)
        if not is_input_valid["is_valid"] and is_input_valid["data"]:
            return is_input_valid["data"]

        is_habit_valid = self._validate_habit(data)
        if not is_habit_valid["is_valid"] and is_input_valid["data"]:
            return is_input_valid["data"]
        habit = is_habit_valid["data"]
        try:
            day = Day.get_by_date(data["date"])
        except ObjectDoesNotExist:
            day = Day(date=data["date"])
            day.save()

        day_habit: DayHabit
        try:
            day_habit = DayHabit.objects.get(habit=habit, day=day)
            DayHabit(
                id=day_habit.pk, habit=habit, day=day, completed=not day_habit.completed
            ).save(force_update=True)
            day_habit = DayHabit.objects.get(habit=habit, day=day)
        except ObjectDoesNotExist:
            DayHabit(habit=habit, day=day, completed=True).save()
            day_habit = DayHabit.objects.get(habit=habit, day=day)

        serializer = DayHabitSerializer(day_habit)
        return ResponseData(status=200, data=serializer.data)
