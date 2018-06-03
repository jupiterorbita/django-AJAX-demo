from __future__ import unicode_literals
from django.db import models
# from datetime import date
# from django.utils import timezone


class Lead(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)  # (default=timezone.now)
    def __repr__(self):
        return "<Lead object: {}, {}, {}, {} >".format(self.first_name, self.last_name, self.email, self.created_at)
