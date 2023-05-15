from django.db import models

from habits.models import Habit

# Create your models here.

class Day(models.Model):
  date = models.DateField()
  habits = models.ManyToManyField(Habit, through="DayHabit")
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self) -> str:
    return self.date.isoformat()

  class Meta:
    db_table = "days" # Change Table Name


class DayHabit(models.Model):
  completed = models.BooleanField(default=False)
  habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
  day = models.ForeignKey(Day, on_delete=models.CASCADE)

  class Meta:
   unique_together = ['habit', 'day']

  def __str__(self) -> str:
    return f"{self.day.date.isoformat()} - {self.habit.name}"