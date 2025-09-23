from django.utils import timezone
from rest_framework.fields import BooleanField, CharField, DateTimeField
from rest_framework.serializers import ModelSerializer, Serializer

from const.const import COMPLETED_ERROR, FORMAT_SERIALIZERS
from const.errors import TASK_ID_NOT_FOUND
from tasks.models import Task


class TaskSerializer(ModelSerializer):
    """
    Сериализатор для модели Task.
    Подходит для всех методов HTTP.
    """

    completed_at = DateTimeField(
        format=FORMAT_SERIALIZERS,
        input_formats=[FORMAT_SERIALIZERS],
        read_only=True,
        default=timezone.now(),
    )
    created_at = DateTimeField(
        format=FORMAT_SERIALIZERS,
        input_formats=[FORMAT_SERIALIZERS],
        read_only=True,
        default=timezone.now(),
    )
    completed = BooleanField(
        default=False,
        error_messages={
            "invalid": COMPLETED_ERROR,
        },
    )

    class Meta:
        model = Task
        fields = (
            "id",
            "title",
            "description",
            "completed",
            "completed_at",
            "created_at",
        )


class TaskErrorSerializer(Serializer):
    detail = CharField(default=TASK_ID_NOT_FOUND)
