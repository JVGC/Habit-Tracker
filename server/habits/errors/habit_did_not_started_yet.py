from habit_tracker.interfaces import UseCaseError


class HabitDidNotStartedYet(UseCaseError):
    def __init__(self) -> None:
        message = "Habit didn't start yet"
        status = "habit_did_not_started_yet"

        super().__init__(message, status)
