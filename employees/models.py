from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    qualification = models.CharField(max_length=50, default="Standard")  # For MVP
    availability = models.TextField()
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)  # Django handles hashing

    def __str__(self):
        return f"{self.first_name} {self.last_name}"