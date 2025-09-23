import os
from datetime import timedelta

from django.contrib.auth.models import User
from django.core.management import BaseCommand
from django.db import transaction
from django.utils import timezone
from faker import Faker
from tqdm import tqdm

from tasks.models import Task


class Command(BaseCommand):
    help = "Команда для создания тестовых данных, и администратора."

    def add_arguments(self, parser):
        parser.add_argument("--count", type=int, default=10000, help="Количество задач для создания")

    def handle(self, *args, **kwargs):
        count = kwargs["count"]
        with transaction.atomic():
            self.create_admin()
            # Количество задач
            self.create_tasks(count)

    def create_admin(self):
        """
        Команда для создания админа.
        :return:
        """
        username = os.getenv("ADMIN_USERNAME")
        password = os.getenv("ADMIN_PASSWORD")

        if not User.objects.filter(username=username).exists():
            user = User.objects.create_superuser(
                email="admin@admin.com",
                first_name="Админ",
                last_name="Админов",
                username=username,
            )
            user.set_password(password)

            self.stdout.write(self.style.SUCCESS(f"Создан администратор c username = {user.username}."))
        else:
            self.stdout.write(self.style.WARNING(f"Администратор с username = {username} уже существует."))

    def create_tasks(self, count):
        fake = Faker("ru_RU")
        tasks = []

        for _ in tqdm(range(count), desc="Создание задач", unit="задача"):
            completed = fake.boolean(chance_of_getting_true=43)
            completed_at = None
            if completed:
                days_ago = fake.random_int(1, 90)
                completed_at = timezone.now() - timedelta(days=days_ago)

            tasks.append(
                Task(
                    title=fake.sentence(nb_words=3).rstrip("."),
                    description=fake.paragraph(nb_sentences=2),
                    completed=completed,
                    completed_at=completed_at,
                )
            )
        # За один запрос создадим все задачи
        Task.objects.bulk_create(tasks)

        self.stdout.write(self.style.SUCCESS(f"Создано {count} задач."))
