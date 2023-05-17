from rest_framework import generics, views
from rest_framework.request import Request
from rest_framework.response import Response
from .models import Habit
from days.models import Day, DayHabit
from .serializers import HabitSerializer
from django.db.models import Sum, Q

class AddNewHabit(generics.CreateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class ListHabits(views.APIView):

    def get(self, request: Request) -> Response:
      requested_date = request.query_params.get('date', None)
      if requested_date:
        habits = Habit.getHabitsByDate(date=request.query_params['date']).annotate(completed=Sum("dayhabit__completed", default=False))
        day = Day.objects.filter(date=request.query_params['date'])
        if day:
          dayHabits = DayHabit.objects.filter(day__id=day[0].id).all()
          for habit in habits:
            if not dayHabits.filter(habit__id=habit.id):
              habit.completed = False
        else:
          for habit in habits:
            habit.completed = False
      else:
        habits = Habit.objects.all()
      serializer = HabitSerializer(habits, many=True)
      return Response(data=serializer.data)

class UpdateHabit(generics.UpdateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    lookup_field = "id"
class DeleteHabit(generics.DestroyAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    lookup_field = "id"