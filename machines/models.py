from django.db import models
from django.urls import reverse

# Create your models here.

class MachineService(models.Model):
    machine_name = models.CharField(max_length=50)
    machine_make = models.CharField(max_length=200)
    service_date = models.DateField()
    next_service_date = models.DateField()
    service_comments = models.TextField()
    serviced_by= models.CharField(max_length=200)

    def __str__(self):
        return self.machine_name

    def get_absolute_url(self):
        return reverse('home')


class MachineReport(models.Model):
    machine_name = models.CharField(max_length=50)
    operator_name = models.CharField(max_length=200)
    maintenance_personnel = models.CharField(max_length=200)
    issue = models.TextField()
    comments = models.TextField()
    report_date = models.DateField()

    def __str__(self):
        return self.machine_name

    def get_absolute_url(self):
        return reverse('home')