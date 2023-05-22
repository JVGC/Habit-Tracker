""" Habits App URLs """
from django.urls import path

from . import views

# this name "urlpatterns" cannot be change to snake case
urlpatterns = [
    path("add", views.AddNewHabit.as_view(), name="AddNewHabit"),
    path("", views.ListHabits.as_view(), name="ListHabits"),
    path("update/<int:id>", views.UpdateHabit.as_view(), name="UpdateHabit"),
    path("delete/<int:id>", views.DeleteHabit.as_view(), name="DeleteHabit"),
]
