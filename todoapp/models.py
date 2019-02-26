from django.db import models


# Create your models here.
class Task(models.Model):

    def __str__(self):
        return self.task_title
    ACTIVE = 'AC'
    COMPLETE = 'CM'
    CLOSED = 'CD'

    STATUS_CHOICES = (
        (ACTIVE, 'Active'),
        (COMPLETE, 'Complete'),
        (CLOSED, 'Closed')
    )
    task_title = models.CharField(max_length=100)
    task_text = models.CharField(max_length=500)
    priority = models.CharField(max_length=200)
    task_status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=ACTIVE)
