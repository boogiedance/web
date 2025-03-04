from django.db import models
from django.contrib import admin
from datetime import datetime
from django.urls import reverse
from django.contrib.auth.models import User  # Для связи статьи с пользователем

class Blog(models.Model):
    title = models.CharField(
        max_length=100,
        db_index=True,
        verbose_name="Заголовок"
    )
    short_content = models.TextField(
        blank=True,
        verbose_name="Краткое содержание"
    )
    content = models.TextField(
        blank=True,
        verbose_name="Полное содержание"
    )
    image = models.ImageField(
        upload_to='blog_images/',
        blank=True,
        null=True,
        verbose_name="Изображение"
    )
    posted = models.DateTimeField(
        default=datetime.now(),
        db_index=True,
        verbose_name="Опубликована"
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Автор статьи",
        related_name="blog_posts",
        null=True,
        blank=True
    ) # Новое поле для связи с пользователем

    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'blog_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ["-posted"]

admin.site.register(Blog)

class Comment(models.Model):
    post = models.ForeignKey('Blog', on_delete=models.CASCADE, related_name="comments", verbose_name="Статья")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    text = models.TextField(verbose_name="Комментарий")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")

    def __str__(self):
        return f"Комментарий от {self.author} к {self.post.title}"