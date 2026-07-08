from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('spaces/', views.spaces, name='spaces'),
    path('details/', views.details, name='details'),
    path('booking/', views.booking, name='booking'),
    path('confirmation/', views.confirmation, name='confirmation'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('reports/', views.reports, name='reports'),
    path('booking/<int:booking_id>/edit/', views.edit_booking, name='edit_booking'),
    path('booking/<int:booking_id>/delete/', views.delete_booking, name='delete_booking'),
]