""" Day App Views """

from datetime import datetime
from rest_framework import generics, views
from rest_framework.response import Response
from rest_framework.request import Request
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Count, Q

from habits.models import Habit
from .serializers import DaySerializer, DayHabitSerializer
from .models import Day, DayHabit


class ListDays(views.APIView):
    """List Days View"""

    def get(self, _: Request) -> Response:
        """GET Request for List Days View"""
        days = (
            Day.objects.all()
            .annotate(completed=Count("dayhabit", filter=Q(dayhabit__completed=True)))
            .order_by("date")
        )

        day_serializer = DaySerializer(days, many=True)
        for day in day_serializer.data:
            day["total"] = len(Habit.get_habits_by_date(day["date"]))
        return Response(status=200, data=day_serializer.data)


class CheckHabit(views.APIView):
    """Check Habit View"""

    def put(self, request: Request) -> Response:
        """PUT Request for Check Habit View"""
        try:
            habit = Habit.objects.get(id=request.data["habit"])
        except ObjectDoesNotExist:
            return Response(status=404, data={"habit": "Habit does not exist"})

        day_serializer = DaySerializer(data={"date": request.data["date"]})
        day_serializer.is_valid(raise_exception=True)

        if datetime.strptime(request.data["date"], "%Y-%m-%d").date() < habit.start_at:
            return Response(status=400, data={"date": "This habit didn't start yet"})

        try:
            day = Day.objects.get(date=request.data["date"])
        except ObjectDoesNotExist:
            day = Day(date=request.data["date"])
            day.save()

        day_habit: DayHabit
        try:
            day_habit = DayHabit.objects.get(habit=habit, day=day)
            DayHabit(
                id=day_habit.pk, habit=habit, day=day, completed=not day_habit.completed
            ).save(force_update=True)
            day_habit = DayHabit.objects.get(habit=habit, day=day)
        except ObjectDoesNotExist:
            DayHabit(habit=habit, day=day, completed=True).save()
            day_habit = DayHabit.objects.get(habit=habit, day=day)
        serializer = DayHabitSerializer(day_habit)
        return Response(data=serializer.data, status=200)
