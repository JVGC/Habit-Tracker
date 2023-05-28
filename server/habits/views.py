""" Habits Django App Views """

from typing import TypedDict, Any
from rest_framework import generics, views
from rest_framework.request import Request
from rest_framework.response import Response

from days.serializers import DaySerializer
from .use_cases.list_date_habits import ListDateHabitsUseCase
from .models.Habit import Habit
from .serializers import HabitSerializer


class AddNewHabit(generics.CreateAPIView):
    """Add New Habit API View"""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


IsValidResponse = TypedDict("is_valid_response", {"is_valid": bool, "data": Any})


class ListHabits(views.APIView):
    """List Habits API View"""

    def _validate(self, input_data):
        day_serializer = DaySerializer(data={"date": input_data["date"]})  # type: ignore
        is_date_valid = day_serializer.is_valid()
        if not is_date_valid:
            return IsValidResponse(
                is_valid=False,
                data={"status": 400, "data": day_serializer.errors},
            )
        return IsValidResponse(is_valid=True, data=None)

    def get(self, request: Request) -> Response:
        """GET Request for List Habits API View"""
        is_input_valid = self._validate(request.query_params)
        if not is_input_valid["is_valid"]:
            response_data = is_input_valid["data"]
            return Response(status=response_data["status"], data=response_data["data"])

        habits = ListDateHabitsUseCase().execute({"date": request.query_params["date"]})
        return Response(data=habits)
