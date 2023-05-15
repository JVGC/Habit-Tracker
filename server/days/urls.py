from django.urls import path
from . import views

urlpatterns = [
    path("add", views.AddNewDay.as_view(), name="AddNewDay")
]