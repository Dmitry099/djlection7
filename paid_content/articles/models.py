from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    has_subscription = models.BooleanField(default=False, verbose_name='Подписка')


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение')
    paid_content = models.BooleanField(default=False, verbose_name='Платный контент')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title
