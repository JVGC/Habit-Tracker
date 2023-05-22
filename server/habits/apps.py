""" Django Habits App Configuration """
from django.apps import AppConfig


class HabitsConfig(AppConfig):
    """Configuration for Habits App"""

    default_auto_field = "django.db.models.BigAutoField"
    name = "habits"
