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
)

urlpatterns = [
    path("", index, name="home-page"),
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("workers/", WorkerListView.as_view(), name="worker-list"),
    path("workers/<int:pk>/", WorkerDetailView.as_view(), name="worker-detail"),
    path("positions/", PositionListView.as_view(), name="position-list"),
    path("positions/<int:pk>/", PositionDetailView.as_view(), name="position-detail"),
    path("task-types/", TaskTypesListView.as_view(), name="task-type-list"),
    path("task-types/<int:pk>/", TaskTypeDetailView.as_view(), name="task-type-detail"),
]

app_name = "catalog"
