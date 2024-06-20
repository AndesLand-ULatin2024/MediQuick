from django.db import models
from django.contrib.postgres.fields import JSONField

class Citas(models.Model):
    date = models.DateField(null=False, blank=False, default=None)
    reason = models.TextField()
    treatment = models.TextField()
    examsData = JSONField(default=dict)

