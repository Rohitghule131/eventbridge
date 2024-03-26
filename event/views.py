from rest_framework.response import Response
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    UpdateAPIView,
)

from .models import Task
from .serializers import TaskSerializer


class ListTaskAPIView(ListAPIView):
    """
    Class for creation of view for list task api.
    """
    permission_classes = ()
    authentication_classes = ()
    serializer_class = TaskSerializer

    def get_queryset(self):
        """
        Method for return task queryset.
        """
        return Task.objects.all().order_by("id")

    def get(self, request, *args, **kwargs):
        """
        GET method for return list of tasks in response.
        """
        task_serializer = super().list(request, *args, **kwargs)

        return Response(task_serializer.data)


class CreateTaskAPIView(CreateAPIView):
    """
    Class for creation of view for create task api.
    """
    permission_classes = ()
    authentication_classes = ()
    serializer_class = TaskSerializer

    def post(self, request, *args, **kwargs):
        """
        POST method for save the task.
        """
        task_serializer = super().post(request, *args, **kwargs)

        return Response(task_serializer.data)


class UpdateTaskAPIView(UpdateAPIView):
    """
    Class for creation of view for update task api.
    """
    permission_classes = ()
    authentication_classes = ()
    serializer_class = TaskSerializer

    def get_object(self):
        """
        Method for return task object.
        """
        return Task.objects.get(id=self.kwargs.get("pk"))

    def patch(self, request, *args, **kwargs):
        """
        PATCH method for update the task.
        """
        try:
            task_serializer = super().patch(request, *args, **kwargs)

            return Response(task_serializer.data)

        except Task.DoesNotExist:
            return Response({"error": "Task does not exist."})

