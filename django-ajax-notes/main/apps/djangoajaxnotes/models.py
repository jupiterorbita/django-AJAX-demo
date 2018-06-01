from __future__ import unicode_literals
from django.db import models
# from datetime import date
# from django.utils import timezone


class Note(models.Model):
    actual_note = models.TextField()
    created_at = models.DateTimeField(auto_now=True)  # (default=timezone.now)
