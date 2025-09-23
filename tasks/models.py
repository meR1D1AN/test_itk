from django.db.models import BooleanField, CharField, DateTimeField, Model, TextField
from django.utils import timezone

from const.models import NULLABLE


class Task(Model):
    """
    Модель задачи.
    """

    title = CharField(
        max_length=200,
        verbose_name="Название задачи",
        help_text="Введите название задачи, максимум 200 символов.",
    )
    description = TextField(
        verbose_name="Описание задачи",
        help_text="Введите описание задачи.",
        blank=True,
    )
    completed = BooleanField(
        verbose_name="Статус задачи",
        help_text="Завершена ли задача?",
        default=False,
    )
    completed_at = DateTimeField(
        verbose_name="Дата завершения задачи",
        **NULLABLE,
    )
    created_at = DateTimeField(
        verbose_name="Дата создания задачи",
        auto_now_add=True,
    )

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
        ordering = ["-created_at"]

    def __str__(self):
        status = "Выполнена" if self.completed else "Не выполнена"
        return f"№-{self.id} {self.title} ({status})"

    def save(self, *args, **kwargs):
        if self.completed is True:
            self.completed_at = timezone.now()
        super().save(*args, **kwargs)
