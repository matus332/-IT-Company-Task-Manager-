from datetime import date, timedelta

from django.test import TestCase

from catalog.models import Task, TaskType, Worker, Position


class TaskModelTest(TestCase):
    def test_task_type_str(self):
        task_type = TaskType.objects.create(
            name="Bug"
        )
        self.assertEqual(str(task_type), "Bug")

    def test_position_str(self):
        position = Position.objects.create(
            name="QA"
        )
        self.assertEqual(str(position), "QA")

    def test_task_str(self):
        task_type = TaskType.objects.create(
            name="Bug"
        )
        task = Task.objects.create(
            name="Fix Dashboard for Vacancies",
            description="Fixed issues in the vacancies dashboard, improved data display and overall functionality.",
            deadline="2026-10-10",
            is_completed=False,
            priority="low",
            task_type=task_type
        )
        self.assertEqual(str(task), "Fix Dashboard for Vacancies")

    def test_task_deadline_is_overdue(self):
        task = Task.objects.create(
            name="Fix Dashboard for Vacancies",
            description="Fixed issues in the vacancies dashboard, improved data display and overall functionality.",
            deadline=date.today() - timedelta(days=1),
            is_completed=False,
            priority="low",
            task_type=TaskType.objects.create(name="Bug")
        )
        self.assertTrue(task.is_overdue)

    def test_task_is_not_overdue_if_deadline_in_future(self):
        task = Task.objects.create(
            name="Test",
            deadline=date.today() + timedelta(days=1),
            is_completed=False,
            priority="low",
            task_type=TaskType.objects.create(name="Bug")
        )
        self.assertFalse(task.is_overdue)

    def test_completed_task_is_not_overdue(self):
        task = Task.objects.create(
            name="Test",
            deadline=date.today() - timedelta(days=1),
            is_completed=True,
            priority="low",
            task_type=TaskType.objects.create(name="Bug")
        )

        self.assertFalse(task.is_overdue)

    def test_worker_str(self):
        position = Position.objects.create(name="Developer")

        worker = Worker.objects.create(
            username="john",
            position=position
        )
        self.assertEqual(
            str(worker),
            "john (Position: Developer)"
        )
