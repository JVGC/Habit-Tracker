# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

from habits.models import Habit


class HabitFactory:
    @staticmethod
    def create_habit(name, start_at):
        Habit(name=name, start_at=start_at).save()
