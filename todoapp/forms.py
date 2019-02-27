from django import forms
from .models import Task


# Form to create new tasks.
class NewTask(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_title', 'task_text', 'task_priority']


# Form to modify existing task.
class ModifyTask(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_title', 'task_text', 'task_priority', 'task_status']


# Form to filter existing tasks.
class FilterTask(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_priority']
