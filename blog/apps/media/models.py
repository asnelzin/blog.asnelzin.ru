# coding=utf-8
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Media(models.Model):
    name = models.CharField('Name', max_length=200)
    image = models.ImageField('Image', upload_to='images/%Y/%m/%d')

    class Meta:
        verbose_name = 'Media'
        verbose_name_plural = 'Media'

    def __str__(self):
        return self.name

