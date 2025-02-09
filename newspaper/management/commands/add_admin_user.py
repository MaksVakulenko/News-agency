from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.core.management.base import BaseCommand
from django.conf import settings



class Command(BaseCommand):
    help = "Set random prices for existing movies"

    def handle(self, *args, **kwargs):
        User: type[AbstractUser] = get_user_model()
        new_user_username = settings.ADMIN_USERNAME
        new_user_email = settings.ADMIN_EMAIL
        new_user_password = settings.ADMIN_PASSWORD
        new_user_first_name = settings.ADMIN_FIRST_NAME
        new_user_last_name = settings.ADMIN_LAST_NAME
        new_user_years_of_experience = settings.ADMIN_YEARS_OF_EXPERIENCE

        user = User.objects.filter(username=new_user_username).first()

        if user:
            self.stdout.write(
                self.style.SUCCESS(f"User {new_user_username} is already exists.")
            )
        else:
            user = User(
                username=new_user_username,
                email=new_user_email,
                is_staff=True,
                is_superuser=True,
                first_name=new_user_first_name,
                last_name=new_user_last_name,
                years_of_experience=new_user_years_of_experience,
            )
            user.set_password(new_user_password)
            user.save()

            self.stdout.write(
                    self.style.SUCCESS(f"User {new_user_username} created.")
                )
