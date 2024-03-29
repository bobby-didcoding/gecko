from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

User = get_user_model()


class DBConfig:
    def manage_super_user(self) -> User:
        user = User.objects.filter(username=settings.SUPERUSER_USERNAME)
        if user.exists():
            pass
        else:
            user = User.objects.create(
                username=settings.SUPERUSER_USERNAME,
                password=make_password(settings.SUPERUSER_PASSWORD),
                is_staff=True,
                is_active=True,
                is_superuser=True,
            )
        return user


def run():
    db_config = DBConfig()
    db_config.manage_super_user()
