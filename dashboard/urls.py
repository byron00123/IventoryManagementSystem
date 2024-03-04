from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name= 'dashboard-index'),
    path('staff/', views.staff, name = 'dashboard-staff')
]