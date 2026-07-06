from django.conf import settings
from django.db import models


def get_post_image_path(instance, filename):
    return f"posts/{instance.author_id}/{filename}"


class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts",
        verbose_name="Автор",
    )
    image = models.ImageField(upload_to=get_post_image_path, verbose_name="Изображение")
    description = models.TextField(blank=True, verbose_name="Описание")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")

    class Meta:
        verbose_name = "Публикация"
        verbose_name_plural = "Публикации"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.author.username} — {self.created_at:%Y-%m-%d %H:%M}"

    @property
    def likes_count(self):
        return self.likes.count()

    @property
    def comments_count(self):
        return self.comments.count()
