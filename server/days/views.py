""" Day App Views """

from typing import TypedDict, Any
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


IsValidResponse = TypedDict("is_valid_response", {"is_valid": bool, "data": Any})


class CheckDayHabit(views.APIView):
    """Check Habit View"""

    def _validate(self, input_data):
        day_serializer = DaySerializer(data={"date": input_data["date"]})  # type: ignore
        is_date_valid = day_serializer.is_valid()
        if not is_date_valid:
            return IsValidResponse(
                is_valid=False,
                data={"status": 400, "data": day_serializer.errors},
            )
        return IsValidResponse(is_valid=True, data=None)

    def put(self, request) -> Response:
        """PUT Request for Check Habit View"""
        is_input_valid = self._validate(request.data)
        if not is_input_valid["is_valid"]:
            response_data = is_input_valid["data"]
            return Response(status=response_data["status"], data=response_data["data"])

        try:
            response_data = CheckDayHabitUseCase().execute(
                {
                    "habit": request.data["habit"],
                    "date": request.data["date"],
                }
            )
            return Response(status=200, data=response_data["data"])
        except HabitDidNotStartedYet as error:
            return Response(status=400, data={"date": error.message})
        except HabitDoesNotExistError as error:
            return Response(status=404, data={"habit": error.message})
