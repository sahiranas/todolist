from django import forms
from django.db import models
from django.forms import fields
from .models import Tasks

class TaskForm(forms.ModelForm):
    class Meta:
        model=Tasks
        fields='__all__'