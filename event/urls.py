from django.urls import path

from .views import (
    ListTaskAPIView,
    CreateTaskAPIView,
    UpdateTaskAPIView,
)

urlpatterns = [
    path("listTasks", ListTaskAPIView.as_view(), name="list-tasks"),
    path("createTask", CreateTaskAPIView.as_view(), name="create-task"),
    path("updateTask/<int:pk>/", UpdateTaskAPIView.as_view(), name="update-task"),
]
