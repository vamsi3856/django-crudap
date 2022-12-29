# tasks/models.py

from django.db import models
from datetime import datetime,date

class Status(models.TextChoices):
    UNSTARTED = 'u', "Not started yet"
    ONGOING = 'o', "Ongoing"
    FINISHED = 'f', "Finished"


class Task(models.Model):
    name = models.CharField(verbose_name="Task name", max_length=65, unique=True)
    status = models.CharField(verbose_name="Task status", max_length=10, choices=Status.choices)
    date = models.DateField("(mm/dd/yy)",auto_now_add=False, auto_now=False ,blank=True,null=True)
    timestramp=models.DateField(auto_now_add=True, auto_now=False ,blank=True)
    def __str__(self):
        return self.name

# tasks/forms.py
from .models import Task
from django import forms

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = "__all__"