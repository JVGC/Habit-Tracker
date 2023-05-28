# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring


from datetime import datetime
from rest_framework.test import APIClient, APITestCase
from habits.models import Habit
from days.models import Day, DayHabit


class ListHabitsTest(APITestCase):
    def test_list_habits_date_incorrect_format(self):
        client = APIClient()
        today = datetime.today()
        response = client.get("/habits/", {"date": today})
        self.assertEqual(response.status_code, 400)
        self.assertIn("Date has wrong format", str(response.data["date"]))

    def test_list_habit_no_habits_for_that_day(self):
        habit_name = "habit1"
        today = datetime.today().date()
        start_at = datetime(today.year + 1, today.month, today.day).date()
        Habit(name=habit_name, start_at=start_at).save()

        client = APIClient()
        response = client.get("/habits/", {"date": today})

        self.assertEqual(len(response.data), 0)

    def test_list_habits_that_start_on_the_sent_date_day_obj_not_created(self):
        habit_name = "habit1"
        start_at = datetime.today().date()
        habit = Habit.objects.create(name=habit_name, start_at=start_at)

        client = APIClient()
        response = client.get("/habits/", {"date": start_at})

        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["id"], habit.pk)
        self.assertEqual(response.data[0]["completed"], False)

    def test_list_habits_that_start_on_the_sent_date_day_obj_created_and_checked(self):
        habit_name = "habit1"
        start_at = datetime.today().date()

        habit = Habit.objects.create(name=habit_name, start_at=start_at)
        day = Day.objects.create(date=start_at)
        DayHabit(habit=habit, day=day, completed=True).save()

        client = APIClient()
        response = client.get("/habits/", {"date": start_at})

        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["id"], habit.pk)
        self.assertEqual(response.data[0]["completed"], True)

    def test_list_habits_checked_day_after_but_not_on_sent_date(self):
        habit_name = "habit1"
        today = datetime.today().date()

        habit = Habit.objects.create(name=habit_name, start_at=today)
        day = Day.objects.create(
            date=datetime(today.year + 1, today.month, today.day).date()
        )
        DayHabit(habit=habit, day=day, completed=True).save()

        client = APIClient()
        response = client.get("/habits/", {"date": today})

        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["id"], habit.pk)
        self.assertEqual(response.data[0]["completed"], False)

    def test_list_habits_checked_day_before_but_not_on_sent_date(self):
        habit_name = "habit1"
        today = datetime.today().date()

        habit = Habit.objects.create(name=habit_name, start_at=today)
        day = Day.objects.create(
            date=datetime(today.year - 1, today.month, today.day).date()
        )
        DayHabit(habit=habit, day=day, completed=True).save()

        client = APIClient()
        response = client.get("/habits/", {"date": today})

        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["id"], habit.pk)
        self.assertEqual(response.data[0]["completed"], False)

    def test_list_habits_just_one_of_two_checked(self):
        habit_name = "habit1"
        start_at = datetime.today().date()

        habit = Habit.objects.create(name=habit_name, start_at=start_at)
        day = Day.objects.create(date=start_at)
        DayHabit(habit=habit, day=day, completed=True).save()

        habit_name = "habit2"
        habit2 = Habit.objects.create(name=habit_name, start_at=start_at)

        client = APIClient()
        response = client.get("/habits/", {"date": start_at})

        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]["id"], habit.pk)
        self.assertEqual(response.data[0]["completed"], True)
        self.assertEqual(response.data[1]["id"], habit2.pk)
        self.assertEqual(response.data[1]["completed"], False)
