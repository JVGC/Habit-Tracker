# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

from datetime import datetime, timedelta
from days.models import Day


class DayFactory:
    @staticmethod
    def create_days_since(date):
        today = datetime.today()
        while date < today:
            Day(date=date.date()).save()
            date = date + timedelta(days=1)


# DayFactory.create_days_since(datetime(2023, 1, 1))
