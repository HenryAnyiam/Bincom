from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime

# Create your models here.

class Task(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")
    title = models.CharField(max_length=250, null=False)
    deadline_date = models.DateField(null=False)
    deadline_time = models.TimeField(null=False)
    created_at = models.DateTimeField(default=timezone.now)

    @property
    def deadline(self):
        """get deadline string"""
        final_deadline = datetime.combine(self.deadline_date, self.deadline_time)
        deadline_date = final_deadline - datetime.now()
        if deadline_date.days < 0 or deadline_date.seconds < 0:
            return "Overdue"
        return f"{deadline_date.days}days {deadline_date.seconds // 60}mins"
