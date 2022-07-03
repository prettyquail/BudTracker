from core.models import Task
from django import forms
from django.forms import ModelForm

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['manager_id','intern_id','deadline','task_name','description']

