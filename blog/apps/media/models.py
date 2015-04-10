# coding=utf-8
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Media(models.Model):
    name = models.CharField('Название', max_length=200)
    image = models.ImageField('Изображение', upload_to='images/%Y/%m/%d')

    class Meta:
        verbose_name = 'медия'
        verbose_name_plural = 'медия'

    def __str__(self):
        return self.name

