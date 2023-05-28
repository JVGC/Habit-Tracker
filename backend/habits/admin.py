""" Django Admin App Habits Configurations """
from django.contrib import admin
from .models.habit import Habit

# Register your models here.

admin.site.register(Habit)
