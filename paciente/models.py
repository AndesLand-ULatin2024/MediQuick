from django.db import models

class Paciente(models.Model):
    name = models.CharField(max_length=250, blank=False, null=False)
    last_name = models.CharField(max_length=250, blank=False, null=False) 
    age = models.PositiveIntegerField(blank=False, null=False)  
    document = models.PositiveBigIntegerField(unique=True, blank=False, null=False, primary_key=True) 
    civil_status = models.CharField(max_length=250, blank=False, null=False)  
    country = models.CharField(max_length=250, blank=False, null=False)
    job = models.CharField(max_length=250, blank=False, null=False)
    address = models.TextField(blank=True, null=True)  

    def __str__(self):
        return f"{self.name} {self.last_name}"