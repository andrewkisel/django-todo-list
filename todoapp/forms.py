from django import forms
from .models import Task


class NewTask(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_title', 'task_text', 'task_priority']


class ModifyTask(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_title', 'task_text', 'task_priority', 'task_status']


class FilterTask(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_priority']
