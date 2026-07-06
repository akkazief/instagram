from django.contrib.auth.models import AbstractUser
from django.db import models


def get_avatar_path(instance, filename):
    return f"avatars/{instance.pk}/{filename}"


class User(AbstractUser):
    class Gender(models.TextChoices):
        MALE = "M", "Мужской"
        FEMALE = "F", "Женский"

    email = models.EmailField(unique=True, verbose_name="Электронная почта")

    avatar = models.ImageField(
        upload_to=get_avatar_path, default="avatars/default.jpg", verbose_name="Аватар"
    )

    bio = models.TextField(blank=True, verbose_name="Информация о пользователе")

    phone = models.CharField(max_length=20, blank=True, verbose_name="Номер телефона")

    gender = models.CharField(
        max_length=1, choices=Gender.choices, blank=True, verbose_name="Пол"
    )

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    @property
    def is_moderator(self):
        return self.groups.filter(name="Moderator").exists()

    @property
    def posts_count(self):
        return self.posts.count()

    @property
    def followers_count(self):
        return self.followers.count()

    @property
    def following_count(self):
        return self.following.count()