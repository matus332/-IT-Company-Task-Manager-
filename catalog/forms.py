from datetime import date

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from .models import Worker, Task, Position, TaskType


class WorkerCreationForm(UserCreationForm):
    username = forms.CharField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = Worker
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "email",
            "position",
        )

    def clean_first_name(self):
        first_name = self.cleaned_data["first_name"]
        return first_name.capitalize()

    def clean_last_name(self):
        last_name = self.cleaned_data["last_name"]
        return last_name.capitalize()


class WorkerUpdateForm(forms.ModelForm):

    class Meta:
        model = Worker
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "position",
        )

    def clean_first_name(self):
        first_name = self.cleaned_data["first_name"]
        return first_name.capitalize()

    def clean_last_name(self):
        last_name = self.cleaned_data["last_name"]
        return last_name.capitalize()


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"

    def clean_deadline(self):
        deadline_now = date.today()
        deadline_in_project = self.cleaned_data["deadline"]
        if deadline_now > deadline_in_project:
            raise ValidationError("The deadline has passed")
        return deadline_in_project

    def clean_name(self):
        name = self.cleaned_data["name"].strip()
        if len(name) < 3:
            raise ValidationError("Task name must be longer than three characters")
        return name


class PositionForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = "__all__"

    def clean_name(self):
        name = self.cleaned_data["name"].strip()
        if len(name) < 3:
            raise ValidationError("Position name must be longer than three characters")
        return name


class TaskTypeForm(forms.ModelForm):
    class Meta:
        model = TaskType
        fields = "__all__"

    def clean_name(self):
        name = self.cleaned_data["name"].strip()
        if len(name) < 3:
            raise ValidationError("Task type name must be longer than three characters")
        return name
