from django.db import models
import sys
sys.path.append("..")
from paciente.models import Paciente

class Citas(models.Model):
    paciente = models.ForeignKey(Paciente, null=False, blank=False, on_delete=models.CASCADE)
    date = models.DateField(null=False, blank=False, default=None)
    reason = models.TextField()
    treatment = models.TextField()
    examsData = models.JSONField(default=dict)

