# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

from datetime import datetime, timedelta
from random import randint, choice

from typing import List
from days.models import DayHabit, Day
from habits.models import Habit


class DayHabitFactory:
    @staticmethod
    def create_day_habits_check(habits: List[int], since):
        today = datetime.today()
        while since < today:
            number_habits_to_be_checked = randint(2, len(habits))

            temp = habits.copy()
            for _ in range(0, number_habits_to_be_checked):
                habit_id = choice(temp)
                temp.remove(habit_id)
                habit = Habit.get_by_id(str(habit_id))
                day = Day.objects.filter(date=since.date())
                DayHabit(habit=habit, day=day[0], completed=True).save()
            since = since + timedelta(days=1)


# DayHabitFactory.create_day_habits_check([1,2,3,4,5], datetime(2023,1,1))
