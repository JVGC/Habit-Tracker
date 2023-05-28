from habit_tracker.errors import UseCaseError


class HabitDidNotStartedYet(UseCaseError):
    def __init__(self) -> None:
        message = "Habit didn't start yet"
        status = "habit_did_not_started_yet"

        super().__init__(message, status)
