from django import forms
from django.forms import ModelForm
from .models import Task

#task-niminen luokka
class TaskForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':'Lisää tehtävä'}))

    class Meta:
        model = Task
        fields = "__all__"
        fields = "__all__"