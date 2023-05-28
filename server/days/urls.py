""" Days App URLs """
from django.urls import path
from . import views

urlpatterns = [
    path("", views.ListDays.as_view(), name="ListDays"),
    path("check", views.CheckDayHabit.as_view(), name="CheckDayHabit"),
]
