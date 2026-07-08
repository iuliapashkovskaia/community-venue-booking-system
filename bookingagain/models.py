from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    name  = models.CharField(max_length=20)
    description  = models.TextField(blank=True)
    capacity = models.PositiveIntegerField()
    
    def __str__(self):
        return self.name
    
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    booking_date = models.DateTimeField()
    hours = models.PositiveIntegerField()
    notes = models.TextField(blank=True)
    
    def __str__(self):
        return f"Booking number {self.id} - {self.room.name} booked by {self.user.username}"


# Create your models here.
