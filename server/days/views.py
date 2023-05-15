from rest_framework import generics, response, views, request
from .serializers import DaySerializer
from .models import Day, DayHabit
from habits.models import Habit
from django.core.exceptions import ObjectDoesNotExist

class AddNewDay(generics.CreateAPIView):
    queryset = Day.objects.all()
    serializer_class = DaySerializer
    lookup_field= "id"

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
          Day.objects.get(date=request.data['date'])
        except ObjectDoesNotExist:
          return response.Response(status=400, data={
             "date": "This date already has a correspondent Day Object"
          })

        return super().create(request, *args, **kwargs)


class ListDays(generics.ListAPIView):
  queryset = Day.objects.all()
  serializer_class = DaySerializer

class CheckHabit(views.APIView):

  def put(self, request: request.Request):
      try:
        habit = Habit.objects.get(id=request.data['habit'])
      except ObjectDoesNotExist:
        return response.Response(status=404, data={
           "habit": "Habit does not exist"
        })

      daySerializer = DaySerializer(data={"date": request.data['date']})
      daySerializer.is_valid(raise_exception=True)

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

      return response.Response(data=dayHabit, status=200)