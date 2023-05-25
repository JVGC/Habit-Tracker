from datetime import datetime
from rest_framework.test import APIClient, APITestCase


class AddHabitTest(APITestCase):
    def test_add_habit_success(self):
        client = APIClient()
        habit_name = "habit1"
        start_at = datetime.today().date()
        request_body = {"name": habit_name, "start_at": start_at}
        response = client.post("/habits/add", data=request_body)
        self.assertEqual(response.status_code, 201)

    def test_add_habit_date_incorrect_format(self):
        client = APIClient()
        habit_name = "habit1"
        start_at = datetime.today()
        request_body = {"name": habit_name, "start_at": start_at}
        response = client.post("/habits/add", data=request_body)
        self.assertEqual(response.status_code, 400)
        self.assertIn("Date has wrong format", str(response.data["start_at"]))

    def test_add_habit_empty_name(self):
        client = APIClient()
        habit_name = ""
        start_at = datetime.today().date()
        request_body = {"name": habit_name, "start_at": start_at}
        response = client.post("/habits/add", data=request_body)
        self.assertEqual(response.status_code, 400)
        self.assertIn("This field may not be blank.", str(response.data["name"]))

    def test_add_habit_missing_fields(self):
        client = APIClient()
        habit_name = "habit_name"
        request_body = {"name": habit_name}
        response = client.post("/habits/add", data=request_body)
        self.assertEqual(response.status_code, 400)
        self.assertIn("This field is required.", str(response.data["start_at"]))
