from django.shortcuts import render
from django.views.generic import CreateView, ListView, TemplateView
from .models import MachineService, MachineReport


# Create your views here.

class ServiceListView(ListView):
    model = MachineService
    template_name = 'service_list.html'
    context_object_name = 'service_list'

class ServiceNewView(CreateView):
    model = MachineService
    template_name = 'service_new.html'
    fields = '__all__'

class ReportNewView(CreateView):
    model = MachineReport
    template_name = 'report_new.html'
    fields = '__all__'

class ReportListView(ListView):
    model = MachineReport
    template_name = 'report_list.html'
    context_object_name = 'report_list'

class HomeView(TemplateView):
    template_name = 'home.html'