from django.urls import path
from catalog.views import (
    index,
    TaskListView,
    WorkerListView,
    PositionListView,
    TaskTypesListView,
    WorkerDetailView,
    TaskDetailView,
    PositionDetailView,
    TaskTypeDetailView,
    PositionCreateView,
    TaskTypeCreateView,
    WorkerCreateView,
    TaskCreateView,
)
urlpatterns = [
    path("", index, name="home-page"),
    #TASKS
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    #WORKERS
    path("workers/", WorkerListView.as_view(), name="worker-list"),
    path("workers/create/", WorkerCreateView.as_view(), name="worker-create"),
    path("workers/<int:pk>/", WorkerDetailView.as_view(), name="worker-detail"),
    #POSITIONS
    path("positions/", PositionListView.as_view(), name="position-list"),
    path("positions/create/", PositionCreateView.as_view(), name="position-create"),
    path("positions/<int:pk>/", PositionDetailView.as_view(), name="position-detail"),
    #TASKTYPES
    path("task-types/", TaskTypesListView.as_view(), name="task-type-list"),
    path("task-types/create/", TaskTypeCreateView.as_view(), name="task-type-create"),
    path("task-types/<int:pk>/", TaskTypeDetailView.as_view(), name="task-type-detail"),
]


app_name = "catalog"
