from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.conf import settings
import os


class Command(BaseCommand):
    def handle(self, *args, **options):
        User = get_user_model()
        user = User.objects.create(
            email=(os.getenv("ADMIN_EMAIL")),
        )
        user.set_password(os.getenv("ADMIN_PASSWORD"))
        user.is_staff = True
        user.is_superuser = True
        user.save()
        self.stdout.write(
            self.style.SUCCESS(f"Successfully created admin user {user.email}")
        )
