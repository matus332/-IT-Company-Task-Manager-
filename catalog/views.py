from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views import generic

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


class WorkerDetailView(generic.DetailView):
    model = Worker


class PositionListView(generic.ListView):
    model = Position


class PositionDetailView(generic.DetailView):
    model = Position


class TaskTypesListView(generic.ListView):
    model = TaskType
    context_object_name = "task_types"


class TaskTypeDetailView(generic.DetailView):
    model = TaskType


class TaskListView(generic.ListView):
    model = Task
    queryset = Task.objects.select_related("task_type").prefetch_related("assignees")


class TaskDetailView(generic.DetailView):
    model = Task
