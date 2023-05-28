""" Habit Did not start yet error """
from habit_tracker.interfaces import UseCaseError


class HabitDidNotStartYet(UseCaseError):
    """Habit Did not start yet error"""

    def __init__(self) -> None:
        message = "Habit didn't start yet"
        status = "habit_did_not_start_yet"

        super().__init__(message, status)
