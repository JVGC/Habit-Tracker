""" List Habits for a Date Use Case Class """
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import ReturnDict

from days.models import DayHabit, Day
from habits.models import Habit
from habits.serializers import HabitSerializer


class ListDateHabitsUseCase:
    """ListDateHabits Use Case Implementation"""

    def __call__(self, date: str = "") -> ReturnDict:
        """List all the habits for a given date"""
        habits = Habit.get_habits_by_date(date=date)
        habits = HabitSerializer(habits, many=True).data
        try:
            day = Day.objects.get(date=date)
            day_habits = DayHabit.objects.filter(day__id=day.pk)
            for habit in habits:
                day_habit = day_habits.filter(habit__id=habit["id"])
                if not day_habit:
                    habit["completed"] = False
                else:
                    habit["completed"] = day_habit[0].completed
        except ObjectDoesNotExist:
            for habit in habits:
                habit["completed"] = False
        return habits
