# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring


from datetime import datetime
from rest_framework.test import APIClient, APITestCase
from habits.models import Habit


class UpdateHabitTest(APITestCase):
    def test_update_habit_success(self):
        habit_name = "habit1"
        start_at = datetime.today().date()
        habit = Habit.objects.create(name=habit_name, start_at=start_at)

        client = APIClient()
        request_body = {"name": habit_name, "start_at": start_at}
        response = client.put(f"/habits/update/{habit.pk}", data=request_body)

        self.assertEqual(response.status_code, 200)

        response_data = response.data
        self.assertEqual(response_data["id"], habit.pk)
        self.assertEqual(response_data["name"], request_body["name"])

    def test_update_habit_date_incorrect_format(self):
        habit_name = "habit1"
        start_at = datetime.today().date()
        habit = Habit.objects.create(name=habit_name, start_at=start_at)

        client = APIClient()
        start_at = datetime.today()
        request_body = {"name": habit_name, "start_at": start_at}
        response = client.put(f"/habits/update/{habit.pk}", data=request_body)

        self.assertEqual(response.status_code, 400)
        self.assertIn("Date has wrong format", str(response.data["start_at"]))

    def test_update_habit_empty_name(self):
        habit_name = "habit1"
        start_at = datetime.today().date()
        habit = Habit.objects.create(name=habit_name, start_at=start_at)

        client = APIClient()
        start_at = datetime.today()
        request_body = {"name": "", "start_at": start_at}

        response = client.put(f"/habits/update/{habit.pk}", data=request_body)

        self.assertEqual(response.status_code, 400)
        self.assertIn("This field may not be blank.", str(response.data["name"]))

    def test_update_habit_missing_fields_put_request(self):
        habit_name = "habit1"
        start_at = datetime.today().date()
        habit = Habit.objects.create(name=habit_name, start_at=start_at)

        client = APIClient()
        habit_name = "habit_name"
        request_body = {"name": habit_name}
        response = client.put(f"/habits/update/{habit.pk}", data=request_body)
        self.assertEqual(response.status_code, 400)
        self.assertIn("This field is required.", str(response.data["start_at"]))

    def test_update_habit_missing_fields_patch_request(self):
        habit_name = "habit1"
        start_at = datetime.today().date()
        habit = Habit.objects.create(name=habit_name, start_at=start_at)

        client = APIClient()
        habit_name = "habit_name"
        request_body = {"name": habit_name}
        response = client.patch(f"/habits/update/{habit.pk}", data=request_body)

        self.assertEqual(response.status_code, 200)

        response_data = response.data
        self.assertEqual(response_data["id"], habit.pk)
        self.assertEqual(response_data["name"], request_body["name"])
