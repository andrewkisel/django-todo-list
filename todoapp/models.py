from django.db import models


# Create your models here.
class Task(models.Model):

    def __str__(self):
        return self.task_title

    # Available values for task status.
    ACTIVE = 'AC'
    INPROGRESS = 'IP'
    CLOSED = 'CD'

    # Available values for task priority.
    LOW = 'LO'
    MEDIUM = 'ME'
    HIGH = 'HI'
    URGENT = 'UR'

    # Tuple for model fields creation.
    STATUS_CHOICES = (
        (ACTIVE, 'Active'),
        (INPROGRESS, 'In Progress'),
        (CLOSED, 'Closed')
    )

    # Tuple for model fields creation.
    PRIORITY_CHOICES = (
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'High'),
        (URGENT, 'Urgent')
    )

    # Create model fields.
    task_title = models.CharField(max_length=100)
    task_text = models.CharField(max_length=500)
    task_priority = models.CharField(max_length=2, choices=PRIORITY_CHOICES, default=LOW)
    task_status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=ACTIVE)
