""" Day App Views """

from rest_framework import views
from rest_framework.response import Response

from habits.errors import HabitDoesNotExistError, HabitDidNotStartYet
from .use_cases import ListDaysUseCase, CheckDayHabitUseCase
from .serializers import DaySerializer


class ListDays(views.APIView):
    """List Days View"""

    def __init__(self):
        self.list_days_use_case = ListDaysUseCase()
        super().__init__()

    def get(self, _) -> Response:
        """GET Request for List Days View"""
        response_data = self.list_days_use_case()
        return Response(status=200, data=response_data)


class CheckDayHabit(views.APIView):
    """Check Habit View"""

    def __init__(self):
        self.check_day_habit_use_case = CheckDayHabitUseCase()
        super().__init__()

    def _validate(self, date=None) -> None:
        """Validate Request params and body.
        Raises Exception if input is not valid
        """
        day_serializer = DaySerializer(data={"date": date})  # type: ignore
        day_serializer.is_valid(raise_exception=True)

    def put(self, request) -> Response:
        """PUT Request for Check Habit View"""
        self._validate(request.data.get("date"))
        try:
            response_data = self.check_day_habit_use_case(
                request.data["habit"], request.data["date"]
            )
            return Response(status=200, data=response_data)
        except HabitDidNotStartYet as error:
            return Response(status=400, data={"date": error.message})
        except HabitDoesNotExistError as error:
            return Response(status=404, data={"habit": error.message})
