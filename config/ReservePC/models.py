from django.db import models
from django.contrib.auth.models import AbstractUser

from .validators import validateNonASCII, validateNonNegativeAndNotZero
# Create your models here.

class User(AbstractUser):
    pass

class Classroom(models.Model):
    name = models.CharField(max_length=64, validators=[validateNonASCII])
    capacity = models.IntegerField(validators=[validateNonNegativeAndNotZero])
    number = models.IntegerField(unique=True)
    def __str__(self):
        return f"{self.name} ({self.capacity})"
    
class Station(models.Model):
    number = models.IntegerField(validators=[validateNonNegativeAndNotZero])
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name="stations")
    def __str__(self):
        return f"{self.classroom.name} - Station {self.number}"
    
class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reservations")
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name="reservations")
    station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name="reservations")
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    def __str__(self):
        return f"{self.user.username} - {self.classroom.name} - {self.station.number} - {self.start_time} - {self.end_time}"