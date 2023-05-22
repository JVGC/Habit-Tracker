from django.urls import path
from . import views

urlpatterns = [
    path("add", views.AddNewDay.as_view(), name="AddNewDay"),
    path("", views.ListDays.as_view(), name="ListDays"),
    path("check", views.CheckHabit.as_view(), name="CheckHabit"),
]
