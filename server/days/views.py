from rest_framework import generics, views
from rest_framework.response import Response
from rest_framework.request import Request
from .serializers import DaySerializer
from .models import Day, DayHabit
from habits.models import Habit
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Count, Q

from datetime import datetime

class AddNewDay(generics.CreateAPIView):
    queryset = Day.objects.all()
    serializer_class = DaySerializer
    lookup_field= "id"

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
          Day.objects.get(date=request.data['date'])
          return Response(status=400, data={
             "date": "This date already has a correspondent Day Object"
          })
        except ObjectDoesNotExist:
          return super().create(request, *args, **kwargs)
class ListDays(views.APIView):

  def get(self, _: Request) -> Response:
    days = Day.objects.all().annotate(completed=Count('dayhabit', filter=Q(dayhabit__completed = True)))

    day_serializer = DaySerializer(days, many=True)
    for day in day_serializer.data:
      day['total'] = len(Habit.getHabitsByDate(day['date']))
    return Response(status=200, data=day_serializer.data)

class CheckHabit(views.APIView):

  def put(self, request: Request) -> Response:
      try:
        habit = Habit.objects.get(id=request.data['habit'])
      except ObjectDoesNotExist:
        return Response(status=404, data={
           "habit": "Habit does not exist"
        })

      daySerializer = DaySerializer(data={"date": request.data['date']})
      daySerializer.is_valid(raise_exception=True)

      if datetime.strptime(request.data['date'], '%Y-%m-%d').date() < habit.start_at:
        return Response(status=400, data={
           "date": "This habit didn't start yet"
        })

      try:
        day = Day.objects.get(date=request.data['date'])
      except ObjectDoesNotExist:
         day = Day(date=request.data['date'])
         day.save()

      dayHabit: DayHabit
      try:
        dayHabit = DayHabit.objects.get(habit=habit, day=day)
        dayHabit = DayHabit(id=dayHabit.pk, habit=habit, day=day, completed=not dayHabit.completed).save(force_update=True)
      except ObjectDoesNotExist:
        dayHabit = DayHabit(habit=habit, day=day, completed=True).save()

      return Response(data=dayHabit, status=200)