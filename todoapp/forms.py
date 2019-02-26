from django import forms


class NewTask(forms.Form):
    task_title = forms.CharField(widget=forms.Textarea, label='task_title')
    task_text = forms.CharField(widget=forms.Textarea, label='task_text')
    task_priority = forms.CharField(widget=forms.Textarea, label='task_priority')
