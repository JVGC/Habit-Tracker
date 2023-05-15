from rest_framework import generics, response
from .serializers import DaySerializer
from .models import Day

class AddNewDay(generics.CreateAPIView):
    queryset = Day.objects.all()
    serializer_class = DaySerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        does_date_exist = Day.objects.filter(date=request.data['date'])
        if does_date_exist:
          return response.Response(status=400, data={
             "date": "This date already has a correspondent Day Object"
          })

        return super().create(request, *args, **kwargs)

