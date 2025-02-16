from django.db import models
from clients.models import Client  # Import the Client model
from employees.models import Employee # Import the Employee Model

class Visit(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    planned_start_time = models.DateTimeField()
    planned_end_time = models.DateTimeField()
    actual_start_time = models.DateTimeField(blank=True, null=True)
    actual_end_time = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Visit to {self.client} by {self.employee} at {self.planned_start_time}"