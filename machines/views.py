from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import MachineService, MachineReport


# Create your views here.

class ServiceListView(ListView):
    model = MachineService
    template_name = 'service_list.html'

class ReportListView(ListView):
    model = MachineReport
    template_name = 'report_list.html'