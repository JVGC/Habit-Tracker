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
    db_table = "habits" # Change Table Name


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

  def __str__(self) -> str:
    return self.day.date.isoformat()