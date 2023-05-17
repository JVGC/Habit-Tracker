from rest_framework import generics, views
from rest_framework.request import Request
from rest_framework.response import Response
from .models import Habit
from .serializers import HabitSerializer
from django.db.models import Sum

class AddNewHabit(generics.CreateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class ListHabits(views.APIView):

    def get(self, request: Request) -> Response:
      requested_date = request.query_params.get('date', None)
      if requested_date:
        habits = Habit.getHabitsByDate(date=request.query_params['date']).annotate(completed=Sum("dayhabit__completed", default=False))
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