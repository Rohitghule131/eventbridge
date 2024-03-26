from django.db import models
from datetime import datetime


class Task(models.Model):
    """
    Class for create a table for storing the task.
    """
    title = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(null=True, blank=False)
    reminder_at = models.DateTimeField(null=True, blank=False)
    scheduler_id = models.CharField(max_length=200, null=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=datetime.utcnow)
    updated_at = models.DateTimeField(auto_now=datetime.utcnow)

    def __str__(self):
        """
        Method for return class name.
        """
        return F"{self.id} - {self.title}"
