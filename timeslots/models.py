import uuid
from django.db import models
from django.db.models import Q
from datetime import datetime, timedelta


class TimeSlotManager(models.Manager):

    def check_for_expired_pendings(self):
        now = datetime.now()
        self.filter(
            status=TimeSlot.Status.PENDING,
            pending_until__lt=now
        ).update(
            status=TimeSlot.Status.AVAILABLE,
            pending_until=None
        )

    def all_future(self):
        today = datetime.today().date()
        now = datetime.now().time()

        return self.filter(
            Q(date__gt=today) | Q(date=today, begin_time__gt=now)
        )

    def all_future_available(self):
        return self.all_future().filter(status=TimeSlot.Status.AVAILABLE)

    def all_available_for_date(self, date):
        now = datetime.now().time()

        return self.filter(
            status=TimeSlot.Status.AVAILABLE,
            date=date,
            begin_time__gt=now
        )


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

    objects = TimeSlotManager()

    def format_range(self):
        return f'{self.begin_time} - {self.end_time}'

    def set_pending(self):
        expiration_time = datetime.now() + timedelta(minutes=20)

        self.pending_until = expiration_time
        self.status = TimeSlot.Status.PENDING
