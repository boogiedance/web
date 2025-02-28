from django.db import models
from django.contrib import admin
from datetime import datetime
from django.urls import reverse


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
    posted = models.DateTimeField(
        default=datetime.now(),
        db_index=True,
        verbose_name="Опубликована"
    )

    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'blog_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ["-posted"]


admin.site.register(Blog)
