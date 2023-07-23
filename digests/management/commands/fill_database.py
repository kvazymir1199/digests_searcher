import csv
import os
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand

from digests.models import (
    User,
    Subscription,
    Post
)


def get_path(path):
    return os.path.join(
        Path(settings.BASE_DIR),
        path
    )


class Command(BaseCommand):
    """Команда для загрузки csv файлов в базу данных:
    python manage.py fill_database"""

    help = "Загрузка информации из csv файлов в базу данных"

    def fill_users(self):
        self.stdout.write(f"Путь: {settings.BASE_DIR}")

        with open(get_path("data/users.csv"), "r",
                  encoding="utf-8") as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                User.objects.get_or_create(name=row[0])

    def fill_subscription(self):
        with open(get_path("data/subscriptions.csv"), "r",
                  encoding="utf-8") as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                Subscription.objects.get_or_create(
                    user_id=row[0],
                    source=row[1]
                )

    def fill_posts(self):
        with open(get_path("data/posts.csv"), "r",
                  encoding="utf-8") as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                Post.objects.get_or_create(
                    subscription_id=row[0],
                    content=row[1],
                    rating=row[2]
                )

    def handle(self, *args, **kwargs):
        self.stdout.write("Подождите. Заполнение базы данных.")
        self.fill_users()
        self.fill_subscription()
        self.fill_posts()
        self.stdout.write("База данных заполнена")
