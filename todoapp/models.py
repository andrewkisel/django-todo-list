from django.db import models


# Create your models here.
class Task(models.Model):
    task_name = models.CharField(max_length=500)
    priority = models.CharField(max_length=200)
