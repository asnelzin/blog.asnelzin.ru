# coding=utf-8
from __future__ import unicode_literals

from datetime import date
from django.core.urlresolvers import reverse

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from taggit.managers import TaggableManager


@python_2_unicode_compatible
class Post(models.Model):
    title = models.CharField('Заголовок', max_length=700)
    body = models.TextField('Контент', blank=True)
    slug = models.SlugField('Слаг', max_length=70, help_text='URL', unique=True)
    date = models.DateField('Дата публикации', default=date.today())

    tags = TaggableManager()

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('content:post_view', args=[self.slug])

