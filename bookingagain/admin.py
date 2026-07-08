from django.contrib import admin
from .models import Room, Booking

admin.site.site_header = "VenueCo Admin"
admin.site.site_title = "VenueCo Admin"
admin.site.index_title = "Booking and Events Management"

admin.site.register(Room)
admin.site.register(Booking)