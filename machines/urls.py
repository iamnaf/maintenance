from django.urls import path
from .views import ServiceListView, ReportListView, HomeView, ServiceNewView, ReportNewView

urlpatterns = [
    path('report_list/', ReportListView.as_view(), name='report_list'),
    path('service_list/', ServiceListView.as_view(), name='service_list'),
    path('report_new/', ReportNewView.as_view(), name='report_new'),
    path('service/new/', ServiceNewView.as_view(), name='service_new'),
    path('', HomeView.as_view(), name='home'),
]