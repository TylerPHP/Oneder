from django.db import models
from datetime import datetime
# default=datetime.now().strftime("%Y-%m-%d %H:%M:%S")


class Clock(models.Model):
    """Model for saving alarms"""
    time = models.DateTimeField(max_length=140)
    description = models.CharField(max_length=300)
    rang = models.BooleanField(default=False)
