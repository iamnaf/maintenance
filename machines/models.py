from django.db import models

# Create your models here.

class Machine(models.Model):
    machine_name = models.CharField(max_length=50)
    machine_make = models.CharField(max_length=200)
    service_date = models.DateField()
    next_service_date = models.DateField()
    service_comments = models.TextField()

    def __str__(self):
        return self.machine_name


class MachineReport(models.Model):
    machine_name = models.CharField(max_length=50)
    operator_name = models.CharField(max_length=200)
    maintenance_personnel = models.CharField(max_length=200)
    issue = models.TextField()
    comments = models.TextField()
    # resolved = models.Choices(value=1)

    def __str__(self):
        return self.machine_name
