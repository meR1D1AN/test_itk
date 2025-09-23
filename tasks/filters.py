from django_filters import (
    BooleanFilter,
    CharFilter,
    DateTimeFromToRangeFilter,
    FilterSet,
)

from const.views import FORMAT_DATE_TIME
from tasks.models import Task


class TaskFilter(FilterSet):
    title = CharFilter(
        field_name="title",
        lookup_expr="iexact",
        label="Фильтрация по названию задачи",
    )
    description = CharFilter(
        field_name="description",
        lookup_expr="iexact",
        label="Фильтрация по описанию задачи",
    )
    completed = BooleanFilter(
        field_name="completed",
        label="Фильтрация по завершенности задачи",
    )
    completed_at = DateTimeFromToRangeFilter(
        field_name="completed_at",
        label=f"Фильтрация от и до даты завершения задачи, {FORMAT_DATE_TIME}",
    )
    created_at = DateTimeFromToRangeFilter(
        field_name="created_at",
        label=f"Фильтрация от и до даты создания задачи, {FORMAT_DATE_TIME}",
    )

    class Meta:
        model = Task
        fields = [
            "title",
            "description",
            "completed",
            "completed_at",
        ]
