import uuid

from django.db import models


class TimeSlot(models.Model):

    class Status(models.TextChoices):
        AVAILABLE = 'A', 'Available'
        PENDING = 'P', 'Pending'
        TAKEN = 'T', 'Taken'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    date = models.DateField()
    begin_time = models.TimeField()
    end_time = models.TimeField()

    status = models.TextField(max_length=1, choices=Status.choices, default=Status.AVAILABLE)
    pending_until = models.DateTimeField(null=True, default=None, editable=False)

    name = models.CharField(max_length=254, null=True, blank=True, default=None)
    email_address = models.EmailField(null=True, blank=True, default=None)
    details = models.TextField(null=True, blank=True, default=None)
