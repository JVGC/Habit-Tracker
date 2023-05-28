# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

from datetime import datetime
from rest_framework.test import APITestCase, APIClient
from days.models import Day, DayHabit
from habits.models import Habit


class ListDaysTest(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()

    def test_list_days_no_habit_registered(self):
        Day(date=datetime.today().date()).save()
        response = self.client.get("/days/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["completed"], 0)
        self.assertEqual(response.data[0]["total"], 0)

    def test_list_days_no_days(self):
        response = self.client.get("/days/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 0)

    def test_list_days_habit_all_habits_are_completed(self):
        today = datetime.today().date()
        day = Day.objects.create(date=today)

        habit = Habit.objects.create(name="habit1", start_at=today)
        habit2 = Habit.objects.create(name="habit2", start_at=today)
        DayHabit(habit=habit, day=day, completed=True).save()
        DayHabit(habit=habit2, day=day, completed=True).save()

        response = self.client.get("/days/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["completed"], 2)
        self.assertEqual(response.data[0]["total"], 2)

    def test_list_days_not_all_habits_are_completed(self):
        today = datetime.today().date()
        day = Day.objects.create(date=today)

        habit = Habit.objects.create(name="habit1", start_at=today)
        Habit(name="habit2", start_at=today).save()
        DayHabit(habit=habit, day=day, completed=True).save()

        response = self.client.get("/days/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["completed"], 1)
        self.assertEqual(response.data[0]["total"], 2)

    def test_list_days_habits_number_differentiate_between_days(self):
        today = datetime.today().date()
        tomorrow = datetime(today.year, today.month, today.day + 1).date()
        day = Day.objects.create(date=today)
        Day(date=tomorrow).save()

        habit = Habit.objects.create(name="habit1", start_at=today)
        Habit(name="habit2", start_at=tomorrow).save()
        DayHabit(habit=habit, day=day, completed=True).save()

        response = self.client.get("/days/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]["completed"], 1)
        self.assertEqual(response.data[0]["total"], 1)
        self.assertEqual(response.data[1]["completed"], 0)
        self.assertEqual(response.data[1]["total"], 2)
