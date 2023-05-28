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

    def _validate(self, input):
        day_serializer = DaySerializer(data={"date": input["date"]})  # type: ignore
        is_date_valid = day_serializer.is_valid()
        if not is_date_valid:
            return IsValidResponse(
                is_valid=False,
                data={"status": 400, "data": day_serializer.errors},
            )
        return IsValidResponse(is_valid=True, data=None)

    def get(self, request: Request) -> Response:
        """GET Request for List Habits API View"""
        requested_date = request.query_params.get("date", None)
        if requested_date:
            is_input_valid = self._validate(request.query_params)
            if is_input_valid["is_valid"]:
                habits = ListDateHabitsUseCase().execute({"date": requested_date})
            else:
                response_data = is_input_valid["data"]
                return Response(
                    status=response_data["status"], data=response_data["data"]
                )
        else:
            habits = Habit.objects.all()
        serializer = HabitSerializer(habits, many=True)
        return Response(data=serializer.data)
