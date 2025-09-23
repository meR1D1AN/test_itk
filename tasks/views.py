from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import (
    OpenApiResponse,
    extend_schema,
    extend_schema_view,
)
from rest_framework.exceptions import NotFound
from rest_framework.viewsets import ModelViewSet

from const.errors import (
    TASK_404,
    TASK_EXAMPLE_400_CREATE,
    TASK_EXAMPLE_400_UPDATE,
    TASK_ID_NOT_FOUND,
)
from const.views import (
    FORMAT_DATE_TIME,
    LIMIT,
    OFFSET,
    TASK_ID,
    TASK_SETTINGS,
)
from tasks.filters import TaskFilter
from tasks.models import Task
from tasks.serializers import TaskSerializer


@extend_schema(tags=[TASK_SETTINGS["name"]])
@extend_schema_view(
    list=extend_schema(
        summary="Список задач",
        description="Получения списка всех задач, с возможностью фильтрации по полям:\n\n"
        "`title` - название задачи;\n\n"
        "`description` - описание задачи;\n\n"
        "`completed` - статус задачи, True/False;\n\n"
        f"`completed_at_after` - от даты выполнения задачи, {FORMAT_DATE_TIME};\n\n"
        f"`completed_at_before` - до даты выполнения задачи, {FORMAT_DATE_TIME};\n\n"
        f"`created_at_after` - от даты создания задачи, {FORMAT_DATE_TIME};\n\n"
        f"`created_at_before` - до даты создания задачи, {FORMAT_DATE_TIME};\n\n"
        "`limit` - количество задач на одной странице (стандартная пагинация 20 задач на страницу);\n\n"
        "`offset` - начальный индекс для пагинации.",
        parameters=[
            LIMIT,
            OFFSET,
        ],
        responses={
            200: OpenApiResponse(
                TaskSerializer(many=True),
                description="Успешное получение списка всех задач",
            ),
        },
    ),
    create=extend_schema(
        summary="Создание задачи",
        description="Создание новой задачи.\n\n"
        "`title` - название задачи, ограничение в 200 символов;\n\n"
        "`description` - название задачи, ограничение нет, так как это поле с описанием;\n\n"
        "Если при создании поле `completed`: `true`, то в ответе получим поле "
        "`completed_at`: `дату и время выполнения задачи`;\n\n"
        "Если при создании поле `completed`: `false`, то в ответе получим поле `completed_at`:`null`;\n\n"
        "`created_at` - дата и время создания задачи;\n\n",
        request=TaskSerializer,
        responses={
            201: OpenApiResponse(
                response=TaskSerializer,
                description="Успешное создание задачи",
            ),
            400: OpenApiResponse(
                response=TaskSerializer,
                description="Ошибки при создании задачи",
                examples=TASK_EXAMPLE_400_CREATE,
            ),
        },
    ),
    retrieve=extend_schema(
        summary="Получение детальной информации о задаче",
        description="Получение детальной информации о задаче по `id`.",
        parameters=[TASK_ID],
        responses={
            200: OpenApiResponse(
                response=TaskSerializer,
                description="Успешное получение детальной информации о задаче",
            ),
            404: TASK_404,
        },
    ),
    update=extend_schema(
        summary="Полное обновление задачи",
        description="Обновление всех полей задачи по `id`.",
        parameters=[TASK_ID],
        request=TaskSerializer,
        responses={
            200: OpenApiResponse(
                response=TaskSerializer,
                description="Успешное полное обновление задачи",
            ),
            400: OpenApiResponse(
                response=TaskSerializer,
                description="Ошибки при обновлении задачи",
                examples=TASK_EXAMPLE_400_UPDATE,
            ),
            404: TASK_404,
        },
    ),
    partial_update=extend_schema(
        summary="Частичное обновление задачи",
        description="Частичное обновление задачи по `id`.",
        parameters=[TASK_ID],
        request=TaskSerializer,
        responses={
            200: OpenApiResponse(
                response=TaskSerializer,
                description="Успешное частичное обновление задачи",
            ),
            400: OpenApiResponse(
                response=TaskSerializer,
                description="Ошибки при частичном обновлении задачи",
                examples=TASK_EXAMPLE_400_UPDATE,
            ),
            404: TASK_404,
        },
    ),
    destroy=extend_schema(
        summary="Удаление задачи",
        description="Полное удаление задачи по `id`.",
        parameters=[TASK_ID],
        responses={
            204: OpenApiResponse(
                description="Успешное удаление задачи",
            ),
            404: TASK_404,
        },
    ),
)
class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backend = [DjangoFilterBackend]
    filterset_class = TaskFilter

    def get_object(self):
        """
        Возвращает объект, если он существует, или 404, если объект не найден с кастомной ошибкой.
        """

        try:
            return Task.objects.get(pk=self.kwargs["pk"])
        except Task.DoesNotExist:
            raise NotFound(TASK_ID_NOT_FOUND) from None
