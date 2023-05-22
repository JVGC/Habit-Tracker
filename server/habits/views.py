""" Habits Django App Views """

from rest_framework import generics, views
from rest_framework.request import Request
from rest_framework.response import Response
from django.db.models import Sum

from days.models import Day, DayHabit
from .models import Habit
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
            habits = Habit.get_habits_by_date(
                date=request.query_params["date"]
            ).annotate(completed=Sum("dayhabit__completed", default=False))
            day = Day.objects.filter(date=request.query_params["date"])
            if day:
                day_habits = DayHabit.objects.filter(day__id=day[0].id).all()
                for habit in habits:
                    if not day_habits.filter(habit__id=habit.id):
                        habit.completed = False
            else:
                for habit in habits:
                    habit.completed = False
        else:
            habits = Habit.objects.all()
        serializer = HabitSerializer(habits, many=True)
        return Response(data=serializer.data)


class UpdateHabit(generics.UpdateAPIView):
    """Update Habit API View"""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    lookup_field = "id"


class DeleteHabit(generics.DestroyAPIView):
    """Delete Habit API View"""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    lookup_field = "id"
