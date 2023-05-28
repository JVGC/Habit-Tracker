""" List Habits for a Date Use Case Class """
from typing import TypedDict
from django.db.models import Sum
from django.core.exceptions import ObjectDoesNotExist

from days.models import DayHabit, Day
from habits.models import Habit
from habits.serializers import HabitSerializer


RequestData = TypedDict("request_data", {"date": str})


class ListDateHabitsUseCase:
    """ListDateHabits Use Case Implementation"""

    def execute(self, data: RequestData):
        """List all the habit for a given date"""
        habits = Habit.get_habits_by_date(date=data["date"]).annotate(
            completed=Sum("dayhabit__completed", default=False)
        )
        habits = HabitSerializer(habits, many=True).data
        try:
            day = Day.objects.get(date=data["date"])
            day_habits = DayHabit.objects.filter(day__id=day.pk)
            for habit in habits:
                if not day_habits.filter(habit__id=habit["id"]):
                    habit["completed"] = False
        except ObjectDoesNotExist:
            for habit in habits:
                habit["completed"] = False
        return habits
