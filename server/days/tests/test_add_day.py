# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

from datetime import datetime
from rest_framework.test import APITestCase, APIClient
from days.models import Day


class AddDayTest(APITestCase):
    def test_add_day_success(self):
        date = datetime.today().date()

        request_body = {"date": date}
        client = APIClient()
        response = client.post("/days/add", data=request_body)

        self.assertEqual(response.status_code, 201)

    def test_add_day_date_incorrect_format(self):
        date = datetime.today()

        request_body = {"date": date}
        client = APIClient()
        response = client.post("/days/add", data=request_body)

        self.assertEqual(response.status_code, 400)
        self.assertIn("Date has wrong format", str(response.data["date"]))

    def test_add_day_date_already_exist(self):
        date = datetime.today().date()

        Day.objects.create(date=date)

        request_body = {"date": date}
        client = APIClient()
        response = client.post("/days/add", data=request_body)

        self.assertEqual(response.status_code, 400)
        self.assertIn(
            "date already has a correspondent Day Object", str(response.data["date"])
        )
