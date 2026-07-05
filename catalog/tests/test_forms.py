from datetime import date, timedelta

from django.test import TestCase

from catalog.forms import TaskForm, PositionForm, TaskTypeForm
from catalog.models import TaskType


class TaskFormTests(TestCase):
    def setUp(self):
        self.task_type = TaskType.objects.create(name="Bug")

    def test_task_form_invalid_if_deadline_in_past(self):
        form_data = {
            "name": "Fix login bug",
            "description": "Fix broken login page",
            "deadline": date.today() - timedelta(days=1),
            "is_completed": False,
            "priority": "medium",
            "task_type": self.task_type.id,
            "assignees": [],
        }

        form = TaskForm(data=form_data)

        self.assertFalse(form.is_valid())
        self.assertIn("deadline", form.errors)

    def test_task_form_valid_if_deadline_today_or_future(self):
        form_data = {
            "name": "Fix login bug",
            "description": "Fix broken login page",
            "deadline": date.today() + timedelta(days=1),
            "is_completed": False,
            "priority": "medium",
            "task_type": self.task_type.id,
            "assignees": [],
        }

        form = TaskForm(data=form_data)

        self.assertTrue(form.is_valid())


class PositionFormTests(TestCase):
    def test_position_form_invalid_if_name_too_short(self):
        form = PositionForm(data={"name": "A"})

        self.assertFalse(form.is_valid())
        self.assertIn("name", form.errors)


class TaskTypeFormTests(TestCase):
    def test_task_type_form_invalid_if_name_too_short(self):
        form = TaskTypeForm(data={"name": "A"})

        self.assertFalse(form.is_valid())
        self.assertIn("name", form.errors)
