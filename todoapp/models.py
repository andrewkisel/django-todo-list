from django.db import models


# Create your models here.
class Task(models.Model):

    def __str__(self):
        return self.task_title
    ACTIVE = 'AC'
    COMPLETE = 'CM'
    CLOSED = 'CD'

    LOW = 'LO'
    MEDIUM = 'ME'
    HIGH = 'HI'
    URGENT = 'UR'

    STATUS_CHOICES = (
        (ACTIVE, 'Active'),
        (COMPLETE, 'Complete'),
        (CLOSED, 'Closed')
    )

    PRIORITY_CHOICES = (
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'High'),
        (URGENT, 'Urgent')
    )

    task_title = models.CharField(max_length=100)
    task_text = models.CharField(max_length=500)
    task_priority = models.CharField(max_length=2, choices=PRIORITY_CHOICES, default=LOW)
    task_status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=ACTIVE)
