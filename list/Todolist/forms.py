from django import forms
from django.forms import Task
from django.forms.widgets import Widget

class TaskForm(forms.ModelForm):
    title=forms.CharField(Widget=forms.TextInput(attrs={'placeholder':'Task title...'}), label=False)
    due=forms.CharField(Widget=forms.TextInput(attrs={'placeholder':'Due date...'}),label=False)

    class Meta:
          model=Task,
          fields=['title','due']