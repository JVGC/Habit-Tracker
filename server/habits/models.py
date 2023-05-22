from django.db import models

# Create your models here.


class Habit(models.Model):
    name = models.CharField(max_length=30)
    start_at = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = "habits"  # Change Table Name

    @staticmethod
    def getHabitsByDate(date):
        return Habit.objects.filter(start_at__lte=date).order_by("start_at")
