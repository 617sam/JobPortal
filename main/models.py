from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('User', 'User'),
        # Add more roles as needed
    ]
    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='User')
    # add additional fields in here

    def __str__(self):
        return f"{self.username}" 
    
    
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

class Company(models.Model):
    CATEGORY_CHOICES = [
        ('Tech', 'Technology'),
        ('Finance', 'Finance'),
        ('Healthcare', 'Healthcare'),
        ('Education', 'Education'),
        ('Retail', 'Retail'),
        ('Other', 'Other'),
    ]
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email = models.EmailField()
    company_size = models.CharField(max_length=50)
    image = models.ImageField(upload_to='company_images/', blank=True, null=True)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='Other')
    socials = models.JSONField(blank=True, null=True, help_text='Social media links in JSON format')
    website = models.URLField()
    
    def __str__(self):
        return self.name
