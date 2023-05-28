""" Check Habit in a Day Use Case Class """
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import ReturnDict

from days.models import Day, DayHabit
from days.serializers import DayHabitSerializer
from habits.models import Habit
from habits.errors import HabitDoesNotExistError, HabitDidNotStartedYet


DATE_FIELD_FORMAT = "%Y-%m-%d"


class CheckDayHabitUseCase:
    """Check Habit Use Case Implementation"""

    @staticmethod
    def get_and_validate_habit(habit_id: str = "", date: str = "") -> Habit:
        """Gets habit by ID and validates if it has started.
        Returns the Habit otherwise it raises an error"""
        try:
            habit = Habit.get_by_id(habit_id)
        except ObjectDoesNotExist as exc:
            raise HabitDoesNotExistError() from exc

        if not habit.has_started(datetime.strptime(date, DATE_FIELD_FORMAT).date()):
            raise HabitDidNotStartedYet()

        return habit

    @staticmethod
    def execute(habit_id: str = "", date: str = "") -> ReturnDict:
        """Marks an habit in a given date as completed if it's not completed
        and as not completed if it's already completed.
        """
        habit = CheckDayHabitUseCase.get_and_validate_habit(habit_id, date)

        try:
            day = Day.get_by_date(date)
        except ObjectDoesNotExist:
            day = Day(date=date)
            day.save()

        try:
            day_habit = DayHabit.objects.get(habit=habit, day=day)
            day_habit.completed = not day_habit.completed
            day_habit.save(force_update=True)
        except ObjectDoesNotExist:
            day_habit = DayHabit(habit=habit, day=day, completed=True)
            day_habit.save()

        serializer = DayHabitSerializer(day_habit)
        return serializer.data
