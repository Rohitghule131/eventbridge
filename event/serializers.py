from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """
    Class for return serialized data.
    """
    class Meta:
        model = Task
        fields = "__all__"


