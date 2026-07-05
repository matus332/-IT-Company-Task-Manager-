from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from catalog.models import Position, TaskType, Task


class ProtectedViewsTests(TestCase):
    def test_task_list_requires_login(self):
        response = self.client.get(reverse("catalog:task-list"))

        self.assertNotEqual(response.status_code, 200)
        self.assertRedirects(
            response,
            f"/accounts/login/?next={reverse('catalog:task-list')}"
        )


class TaskListViewTests(TestCase):
    def setUp(self):
        self.position = Position.objects.create(name="Developer")
        self.user = get_user_model().objects.create_user(
            username="john",
            password="test12345",
            position=self.position,
        )
        self.client.force_login(self.user)

        self.task_type = TaskType.objects.create(name="Bug")
        self.task = Task.objects.create(
            name="Fix bug",
            description="Fix login bug",
            deadline="2030-01-01",
            priority="medium",
            task_type=self.task_type,
        )

    def test_task_list_view_status_code(self):
        response = self.client.get(reverse("catalog:task-list"))

        self.assertEqual(response.status_code, 200)

    def test_task_list_uses_correct_template(self):
        response = self.client.get(reverse("catalog:task-list"))

        self.assertTemplateUsed(response, "catalog/task_list.html")

    def test_task_list_contains_task(self):
        response = self.client.get(reverse("catalog:task-list"))

        self.assertContains(response, self.task.name)
