from django.db import models
from visits.models import Visit # Import the Visit model

class Attendance(models.Model):
    ARRIVAL = 'arrival'
    DEPARTURE = 'departure'
    TYPE_CHOICES = (
        (ARRIVAL, 'Arrival'),
        (DEPARTURE, 'Departure'),
    )
    visit = models.ForeignKey(Visit, on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"{self.type} at {self.timestamp} for {self.visit}"