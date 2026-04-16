from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    STATUS_CHOICES = [
        ('todo', 'მოსამზადებელი'),
        ('in_progress', 'პროცესშია'),
        ('done', 'დასრულებული'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='todo')
    deadline = models.DateField(null=True, blank=True)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    created_at = models.DateTimeField(auto_now_add=True)