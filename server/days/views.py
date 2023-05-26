""" Day App Views """

from rest_framework import views
from rest_framework.response import Response

from .use_cases import ListDaysUseCase, CheckHabitUseCase


class ListDays(views.APIView):
    """List Days View"""

    def get(self, _) -> Response:
        """GET Request for List Days View"""
        response_data = ListDaysUseCase().execute()
        return Response(status=response_data["status"], data=response_data["data"])


class CheckHabit(views.APIView):
    """Check Habit View"""

    def put(self, request) -> Response:
        """PUT Request for Check Habit View"""
        response_data = CheckHabitUseCase().execute(
            {
                "habit": request.data["habit"],
                "date": request.data.get("date", ""),
            }
        )
        return Response(status=response_data["status"], data=response_data["data"])
