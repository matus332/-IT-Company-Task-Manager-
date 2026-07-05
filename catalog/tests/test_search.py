from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from catalog.models import Position, TaskType, Task


class TaskSearchTests(TestCase):
    def setUp(self):
        self.position = Position.objects.create(name="Developer")
        self.user = get_user_model().objects.create_user(
            username="john",
            password="test12345",
            position=self.position,
        )
        self.client.force_login(self.user)

        self.task_type = TaskType.objects.create(name="Bug")

        Task.objects.create(
            name="Fix login bug",
            description="Login problem",
            deadline="2030-01-01",
            priority="medium",
            task_type=self.task_type,
        )
        Task.objects.create(
            name="Create dashboard",
            description="Dashboard page",
            deadline="2030-01-01",
            priority="medium",
            task_type=self.task_type,
        )

    def test_search_task_by_name(self):
        response = self.client.get(
            reverse("catalog:task-list"),
            {"name": "login"},
        )

        self.assertContains(response, "Fix login bug")
        self.assertNotContains(response, "Create dashboard")


class WorkerSearchTests(TestCase):
    def setUp(self):
        self.position = Position.objects.create(name="Developer")
        self.user = get_user_model().objects.create_user(
            username="admin",
            password="test12345",
            position=self.position,
        )
        self.client.force_login(self.user)

        get_user_model().objects.create_user(username="john")
        get_user_model().objects.create_user(username="mark")

    def test_search_worker_by_username(self):
        response = self.client.get(
            reverse("catalog:worker-list"),
            {"username": "john"},
        )

        self.assertContains(response, "john")
        self.assertNotContains(response, "mark")


class PositionSearchTests(TestCase):
    def setUp(self):
        self.position = Position.objects.create(name="Developer")
        self.user = get_user_model().objects.create_user(
            username="admin",
            password="test12345",
            position=self.position,
        )
        self.client.force_login(self.user)

        Position.objects.create(name="Designer")

    def test_search_position_by_name(self):
        response = self.client.get(
            reverse("catalog:position-list"),
            {"name": "dev"},
        )

        self.assertContains(response, "Developer")
        self.assertNotContains(response, "Designer")


class TaskTypeSearchTests(TestCase):
    def setUp(self):
        self.position = Position.objects.create(name="Developer")
        self.user = get_user_model().objects.create_user(
            username="admin",
            password="test12345",
            position=self.position,
        )
        self.client.force_login(self.user)

        TaskType.objects.create(name="Bug")
        TaskType.objects.create(name="Feature")

    def test_search_task_type_by_name(self):
        response = self.client.get(
            reverse("catalog:task-type-list"),
            {"name": "bug"},
        )

        self.assertContains(response, "Bug")
        self.assertNotContains(response, "Feature")