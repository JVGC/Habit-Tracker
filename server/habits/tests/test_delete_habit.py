# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring


from datetime import datetime
from rest_framework.test import APIClient, APITestCase
from habits.models import Habit
from days.models import Day, DayHabit
from django.core.exceptions import ObjectDoesNotExist


class DeleteHabitTest(APITestCase):
    def test_delete_habit_success(self):
        habit_name = "habit1"
        start_at = datetime.today().date()
        habit = Habit.objects.create(name=habit_name, start_at=start_at)

        client = APIClient()
        response = client.delete(f"/habits/delete/{habit.pk}")

        self.assertEqual(response.status_code, 204)
        self.assertRaises(ObjectDoesNotExist, Habit.objects.get, id=habit.pk)

    def test_delete_habit_does_not_exist(self):
        client = APIClient()
        response = client.delete("/habits/delete/123")

        self.assertEqual(response.status_code, 404)

    def test_delete_habit_that_was_checked_at_least_once(self):
        habit_name = "habit1"
        start_at = datetime.today().date()
        habit = Habit.objects.create(name=habit_name, start_at=start_at)
        day = Day.objects.create(date=start_at)
        DayHabit(habit=habit, day=day, completed=True).save()

        client = APIClient()
        response = client.delete(f"/habits/delete/{habit.pk}")

        self.assertEqual(response.status_code, 204)
        self.assertRaises(
            ObjectDoesNotExist, DayHabit.objects.get, habit=habit, day=day
        )
