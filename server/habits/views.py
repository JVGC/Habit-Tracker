from rest_framework import generics
from .models import Habit
from .serializers import HabitSerializer

class AddNewHabit(generics.CreateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

class ListHabits(generics.ListAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer