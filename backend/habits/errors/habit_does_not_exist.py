"""Habit does not exist error"""


class HabitDoesNotExistError(BaseException):
    """Habit does not exist error"""

    def __init__(self) -> None:
        self.message = "Habit does not exist"
