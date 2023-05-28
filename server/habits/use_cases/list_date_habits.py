""" List Habits for a Date Use Case Class """
from django.db.models import Sum
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import ReturnDict

from habit_tracker.interfaces import UseCase
from days.models import DayHabit, Day
from habits.models import Habit
from habits.serializers import HabitSerializer


class ListDateHabitsUseCase(UseCase):
    """ListDateHabits Use Case Implementation"""

    @staticmethod
    def execute(date: str = "") -> ReturnDict:
        """List all the habits for a given date"""
        habits = Habit.get_habits_by_date(date=date).annotate(
            completed=Sum("dayhabit__completed", default=False)
        )
        habits = HabitSerializer(habits, many=True).data
        try:
            day = Day.objects.get(date=date)
            day_habits = DayHabit.objects.filter(day__id=day.pk)
            for habit in habits:
                if not day_habits.filter(habit__id=habit["id"]):
                    habit["completed"] = False
        except ObjectDoesNotExist:
            for habit in habits:
                habit["completed"] = False
        return habits
