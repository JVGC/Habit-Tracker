""" Django Admin App Days Configurations """

from django.contrib import admin
from .models import Day, DayHabit

admin.site.register(Day)
admin.site.register(DayHabit)
