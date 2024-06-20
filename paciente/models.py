from django.db import models

class Paciente(models.Model):
    name = models.CharField(max_length=250, blank=False, null=False)
    lasName =  models.CharField(max_length=250, blank=False, null=False)
    age = models.IntegerField(blank=False, null=False)
    document = models.PositiveBigIntegerField(unique=True, blank=False, editable=False, primary_key=True, default=None)
    civilStatus = models.CharField(max_length=250, blank=False, null=False)
    country = models.CharField(max_length=250, blank=False, null=False)
    job = models.CharField(max_length=250, blank=False, null=False)
    address = models.TextField()


    
