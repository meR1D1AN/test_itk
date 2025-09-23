from drf_spectacular.utils import OpenApiExample, OpenApiResponse

from const.const import COMPLETED_ERROR, TASK_ID_NOT_FOUND, TITLE_MAX_200, TITLE_NULL
from tasks.serializers import TaskErrorSerializer

TASK_EXAMPLE_400_CREATE = [
    OpenApiExample(
        response_only=True,
        name=COMPLETED_ERROR,
        value={"completed": [COMPLETED_ERROR]},
    ),
    OpenApiExample(
        response_only=True,
        name="Ошибка: `title` превышает 200 символов",
        value={"title": [TITLE_MAX_200]},
    ),
    OpenApiExample(
        response_only=True,
        name="Ошибка: `title` не может быть пустым",
        value={"title": [TITLE_NULL]},
    ),
]

TASK_EXAMPLE_400_UPDATE = [
    OpenApiExample(
        response_only=True,
        name=COMPLETED_ERROR,
        value={"completed": [COMPLETED_ERROR]},
    ),
    OpenApiExample(
        response_only=True,
        name="Ошибка: `title` превышает 200 символов",
        value={"title": [TITLE_MAX_200]},
    ),
    OpenApiExample(
        response_only=True,
        name="Ошибка: `title` не может быть пустым",
        value={"title": [TITLE_NULL]},
    ),
]

TASK_404 = OpenApiResponse(
    response=TaskErrorSerializer,
    description="Ошибка: задача не найдена",
    examples=[
        OpenApiExample(
            name="Ошибка: задача не найдена",
            value={"detail": TASK_ID_NOT_FOUND},
            response_only=True,
        )
    ],
)
