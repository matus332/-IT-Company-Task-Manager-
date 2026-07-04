from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from catalog.models import Task, Worker, Position


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
