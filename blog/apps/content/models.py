# coding=utf-8
from __future__ import unicode_literals

from datetime import date

from django.db import models

from taggit.managers import TaggableManager


class Post(models.Model):
    title = models.CharField('Заголовок', max_length=700)
    body = models.TextField('Контент', blank=True)
    slug = models.SlugField('Слаг', max_length=70, help_text='URL', unique=True)
    date = models.DateField('Дата публикации', default=date.today())

    tags = TaggableManager()

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'

