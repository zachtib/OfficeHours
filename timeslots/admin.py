from django.contrib import admin
from timeslots.models import TimeSlot


@admin.register(TimeSlot)
class TimeSlotAdmin(admin.ModelAdmin):
    pass

