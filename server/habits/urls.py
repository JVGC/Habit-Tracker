from django.urls import path

from . import views

# this name "urlpatterns" cannot be change to snake case
urlpatterns = [
    path("create", views.AddNewHabit.as_view(), name="CreateNewHabit")
]