from django.urls import path
from catalog.views import (
    index,
    TaskListView,
    TaskCreateView,
    TaskDetailView,
    TaskUpdateView,
    WorkerListView,
    WorkerCreateView,
    WorkerDetailView,
    WorkerUpdateView,
    PositionListView,
    PositionCreateView,
    PositionDetailView,
    PositionUpdateView,
    TaskTypesListView,
    TaskTypeCreateView,
    TaskTypeDetailView,
    TaskTypeUpdateView,
)
urlpatterns = [
    path("", index, name="home-page"),
    # TASKS
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    # WORKERS
    path("workers/", WorkerListView.as_view(), name="worker-list"),
    path("workers/create/", WorkerCreateView.as_view(), name="worker-create"),
    path("workers/<int:pk>/", WorkerDetailView.as_view(), name="worker-detail"),
    path("workers/<int:pk>/update/", WorkerUpdateView.as_view(), name="worker-update"),
    # POSITIONS
    path("positions/", PositionListView.as_view(), name="position-list"),
    path("positions/create/", PositionCreateView.as_view(), name="position-create"),
    path("positions/<int:pk>/", PositionDetailView.as_view(), name="position-detail"),
    path("positions/<int:pk>/update/", PositionUpdateView.as_view(), name="position-update"),
    # TASKTYPES
    path("task-types/", TaskTypesListView.as_view(), name="task-type-list"),
    path("task-types/create/", TaskTypeCreateView.as_view(), name="task-type-create"),
    path("task-types/<int:pk>/", TaskTypeDetailView.as_view(), name="task-type-detail"),
    path("task-types/<int:pk>/update/", TaskTypeUpdateView.as_view(), name="task-type-update"),
]


app_name = "catalog"
