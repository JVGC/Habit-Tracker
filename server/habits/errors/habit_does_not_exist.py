from habit_tracker.errors import UseCaseError


class HabitDoesNotExistError(UseCaseError):
    def __init__(self) -> None:
        message = "Habit does not exist"
        status = "habit_does_not_exist"

        super().__init__(message, status)
