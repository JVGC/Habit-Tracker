""" List Habits for a Date Use Case Class """
from typing import TypedDict
from django.db.models import Sum

from days.models import DayHabit, Day
from habits.models import Habit


RequestData = TypedDict("request_data", {"date": str})


class ListDateHabitsUseCase:
    """ListDateHabits Use Case Implementation"""

    def execute(self, data: RequestData):
        """List all the habit for a given date"""
        habits = Habit.get_habits_by_date(date=data["date"]).annotate(
            completed=Sum("dayhabit__completed", default=False)
        )
        day = Day.objects.filter(date=data["date"])
        if day:
            day_habits = DayHabit.objects.filter(day__id=day[0].pk).all()
            for habit in habits:
                if not day_habits.filter(habit__id=habit.pk):
                    habit.completed = False
        else:
            for habit in habits:
                habit.completed = False
        return habits
