from django.contrib import admin
from .models import Machine, MachineReport

# Register your models here.
admin.site.register(Machine)
admin.site.register(MachineReport)