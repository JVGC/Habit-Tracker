from rest_framework import generics
from .serializers import DaySerializer
from .models import Day

class AddNewDay(generics.CreateAPIView):
    queryset = Day.objects.all()
    serializer_class = DaySerializer

# Create your views here.
