""" Habits Django App Views """

from rest_framework import generics, views
from rest_framework.request import Request
from rest_framework.response import Response
from django.db.models import Sum

from days.models import Day, DayHabit
from .use_cases.list_date_habits import ListDateHabitsUseCase
from .models.Habit import Habit
from .serializers import HabitSerializer


class AddNewHabit(generics.CreateAPIView):
    """Add New Habit API View"""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class ListHabits(views.APIView):
    """List Habits API View"""

    def get(self, request: Request) -> Response:
        """GET Request for List Habits API View"""
        requested_date = request.query_params.get("date", None)
        if requested_date:
            habits = ListDateHabitsUseCase().execute({"date": requested_date})
        else:
            habits = Habit.objects.all()
        serializer = HabitSerializer(habits, many=True)
        return Response(data=serializer.data)
