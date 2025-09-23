from django.contrib.admin import ModelAdmin, register

from tasks.models import Task


@register(Task)
class TaskAdmin(ModelAdmin):
    list_display = ["title", "completed", "created_at", "completed_at"]
    list_filter = ["completed", "created_at", "completed_at"]
    search_fields = ["title", "description"]
