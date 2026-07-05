from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from catalog.forms import WorkerCreationForm
from catalog.models import Task, Worker, Position, TaskType


def index(request):
    num_tasks = Task.objects.count()
    num_worker = Worker.objects.count()
    num_position = Position.objects.count()
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_tasks": num_tasks,
        "num_worker": num_worker,
        "num_position": num_position,
        "num_visits": num_visits + 1
    }

    return render(request, "catalog/index.html", context=context)


class WorkerListView(generic.ListView):
    model = Worker
    queryset = Worker.objects.all().select_related("position")


class WorkerCreateView(generic.CreateView):
    model = Worker
    form_class = WorkerCreationForm
    success_url = reverse_lazy("catalog:worker-list")


class WorkerDetailView(generic.DetailView):
    model = Worker


class WorkerUpdateView(generic.UpdateView):
    model = Worker
    fields = ("username", "first_name", "last_name", "email", "position")
    success_url = reverse_lazy("catalog:worker-list")


class WorkerDeleteView(generic.DeleteView):
    model = Worker
    success_url = reverse_lazy("catalog:worker-list")


class TaskTypesListView(generic.ListView):
    model = TaskType
    context_object_name = "task_types"


class TaskTypeCreateView(generic.CreateView):
    model = TaskType
    fields = "__all__"
    success_url = reverse_lazy("catalog:task-type-list")


class TaskTypeDetailView(generic.DetailView):
    model = TaskType


class TaskTypeUpdateView(generic.UpdateView):
    model = TaskType
    fields = "__all__"
    success_url = reverse_lazy("catalog:task-type-list")


class TaskTypeDeleteView(generic.DeleteView):
    model = TaskType
    success_url = reverse_lazy("catalog:task-type-list")


class PositionListView(generic.ListView):
    model = Position


class PositionCreateView(generic.CreateView):
    model = Position
    fields = "__all__"
    success_url = reverse_lazy("catalog:position-list")


class PositionDetailView(generic.DetailView):
    model = Position


class PositionUpdateView(generic.UpdateView):
    model = Position
    fields = "__all__"
    success_url = reverse_lazy("catalog:position-list")


class PositionDeleteView(generic.DeleteView):
    model = Position
    success_url = reverse_lazy("catalog:position-list")


class TaskListView(generic.ListView):
    model = Task
    queryset = (
        Task.objects
        .select_related("task_type")
        .prefetch_related("assignees")
    )


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("catalog:task-list")


class TaskDetailView(generic.DetailView):
    model = Task


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("catalog:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("catalog:task-list")
