from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    pass
    # add additional fields in here

    def __str__(self):
        return self.username
    
    
class Job(models.Model):
    LEVEL_CHOICES = [
        ('Entry', 'Entry Level'),
        ('Mid', 'Mid Level'),
        ('Senior', 'Senior Level'),
        ('Lead', 'Lead'),
    ]
    
    name = models.CharField(max_length=255)
    details = models.TextField()
    address = models.CharField(max_length=255)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=255)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    
    openings = models.PositiveIntegerField()
    

    def __str__(self):
        return self.name
