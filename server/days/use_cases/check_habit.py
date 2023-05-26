""" Check Habit in a Day Use Case Class """
from typing import TypedDict
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist

from days.models import Day, DayHabit
from days.serializers import DaySerializer, DayHabitSerializer
from habits.models import Habit


RequestData = TypedDict("request_data", {"habit": str, "date": str})
ResponseData = TypedDict("response_data", {"status": int, "data": dict[str, str]})


class CheckHabitUseCase:
    """Check Habit Use Case Implementation"""

    def execute(self, data: RequestData) -> ResponseData:
        """Marks an habit in a given date as completed if it's completed
        and as not completed if it's already completed.
        """
        try:
            habit = Habit.objects.get(id=data["habit"])
        except ObjectDoesNotExist:
            return ResponseData(status=404, data={"habit": "Habit does not exist"})

        day_serializer = DaySerializer(data={"date": data["date"]})
        day_serializer.is_valid(raise_exception=True)

        if datetime.strptime(data["date"], "%Y-%m-%d").date() < habit.start_at:
            return ResponseData(
                status=400, data={"date": "This habit didn't start yet"}
            )

        try:
            day = Day.objects.get(date=data["date"])
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
