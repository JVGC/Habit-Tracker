""" Habit Did not start yet error """


class HabitDidNotStartYet(BaseException):
    """Habit Did not start yet error"""

    def __init__(self) -> None:
        self.message = "Habit didn't start yet"
