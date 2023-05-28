"""Habit does not exist error"""
from habit_tracker.interfaces import UseCaseError


class HabitDoesNotExistError(UseCaseError):
    """Habit does not exist error"""

    def __init__(self) -> None:
        message = "Habit does not exist"
        status = "habit_does_not_exist"

        super().__init__(message, status)
