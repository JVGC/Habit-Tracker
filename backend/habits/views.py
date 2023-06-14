""" Habits Django App Views """

from rest_framework import generics, views
from rest_framework.request import Request
from rest_framework.response import Response

from days.serializers import DaySerializer
from .use_cases.list_date_habits import ListDateHabitsUseCase
from .models.habit import Habit
from .serializers import HabitSerializer


class AddNewHabit(generics.CreateAPIView):
    """Add New Habit API View"""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class ListHabits(views.APIView):
    """List Habits API View"""

    def __init__(self):
        self.list_date_habits_use_case = ListDateHabitsUseCase()
        super().__init__()

    def _validate(self, input_data) -> None:
        """Validate Request params and body.
        Raises Exception if input is not valid
        """
        day_serializer = DaySerializer(data={"date": input_data["date"]})  # type: ignore
        day_serializer.is_valid(raise_exception=True)

    def get(self, request: Request) -> Response:
        """GET Request for List Habits API View"""
        self._validate(request.query_params)

        habits = self.list_date_habits_use_case(request.query_params["date"])
        return Response(data=habits)
