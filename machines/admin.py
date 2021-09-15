from django.contrib import admin
from .models import MachineService, MachineReport

# Register your models here.
admin.site.register(MachineService)
admin.site.register(MachineReport)