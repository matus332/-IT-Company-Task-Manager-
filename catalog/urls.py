from django.urls import path
from catalog.views import (
    index,
    TaskListView,
    WorkerListView,
    PositionListView,
    TaskTypesListView,
)

urlpatterns = [
    path("", index, name="home-page"),
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("workers/", WorkerListView.as_view(), name="worker-list"),
    path("positions/", PositionListView.as_view(), name="position-list"),
    path("task-types/", TaskTypesListView.as_view(), name="task-type-list")
]

app_name = "catalog"
