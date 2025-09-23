from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter

TASK_SETTINGS = {
    "name": "Задачи",
    "description": "Методы для работы с задачами",
}

LIMIT = OpenApiParameter(
    name="limit",
    type=OpenApiTypes.INT,
    description="Количество задач на одной странице",
    required=False,
)
OFFSET = OpenApiParameter(
    name="offset",
    type=OpenApiTypes.INT,
    description="Начальный индекс для пагинации",
    required=False,
)

FORMAT_DATE_TIME = "формат: YYYY-MM-DD HH:MM:SS"

TASK_ID = OpenApiParameter(
    name="id",
    type=OpenApiTypes.INT,
    location=OpenApiParameter.PATH,
    description="ID задачи",
    required=True,
)
