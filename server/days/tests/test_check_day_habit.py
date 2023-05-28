# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
from datetime import datetime
from rest_framework.test import APITestCase, APIClient
from habits.models import Habit
from days.models import Day, DayHabit


class CheckDayHabitTest(APITestCase):
    def test_check_day_habit_does_not_exist(self):
        client = APIClient()
        request_body = {"habit": "1", "date": datetime.today().date()}
        response = client.put("/days/check", data=request_body)

        self.assertEqual(response.status_code, 404)

    def test_check_day_habit_date_format_is_invalid(self):
        habit = Habit.objects.create(name="habit1", start_at=datetime.today().date())

        client = APIClient()
        request_body = {"habit": habit.pk, "date": datetime.today()}
        response = client.put("/days/check", data=request_body)

        self.assertEqual(response.status_code, 400)
        self.assertIn("Date has wrong format", str(response.data["date"]))

    def test_check_day_habit_did_not_started_yet(self):
        today = datetime.today().date()
        habit = Habit.objects.create(name="habit1", start_at=today)

        client = APIClient()
        request_body = {
            "habit": habit.pk,
            "date": datetime(today.year - 1, today.month, today.day).date(),
        }
        response = client.put("/days/check", data=request_body)

        self.assertEqual(response.status_code, 400)
        self.assertIn("This habit didn't start yet", str(response.data["date"]))

    def test_check_day_habit_day_obj_does_not_exist(self):
        today = datetime.today().date()
        habit = Habit.objects.create(name="habit1", start_at=today)

        client = APIClient()
        request_body = {
            "habit": habit.pk,
            "date": today,
        }
        response = client.put("/days/check", data=request_body)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Day.get_by_date(date=today).date, today)

    def test_check_day_habit_already_checked(self):
        today = datetime.today().date()
        habit = Habit.objects.create(name="habit1", start_at=today)
        day = Day.objects.create(date=today)
        DayHabit(habit=habit, day=day, completed=True).save()

        client = APIClient()
        request_body = {"habit": habit.pk, "date": today}
        response = client.put("/days/check", data=request_body)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["completed"], False)

    def test_check_day_habit_never_checked_before(self):
        today = datetime.today().date()
        habit = Habit.objects.create(name="habit1", start_at=today)

        client = APIClient()
        request_body = {"habit": habit.pk, "date": today}
        response = client.put("/days/check", data=request_body)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["completed"], True)
        self.assertEqual(Day.get_by_date(date=today).date, today)
