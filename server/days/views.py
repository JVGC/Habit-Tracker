""" Day App Views """

from rest_framework import views
from rest_framework.response import Response

from habits.errors import HabitDoesNotExistError, HabitDidNotStartedYet
from .use_cases import ListDaysUseCase, CheckDayHabitUseCase
from .serializers import DaySerializer


class ListDays(views.APIView):
    """List Days View"""

    def get(self, _) -> Response:
        """GET Request for List Days View"""
        response_data = ListDaysUseCase().execute()
        return Response(status=response_data["status"], data=response_data["data"])


class CheckDayHabit(views.APIView):
    """Check Habit View"""

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
            response_data = CheckDayHabitUseCase.execute(
                request.data["habit"], request.data["date"]
            )
            return Response(status=200, data=response_data)
        except HabitDidNotStartedYet as error:
            return Response(status=400, data={"date": error.message})
        except HabitDoesNotExistError as error:
            return Response(status=404, data={"habit": error.message})
