# coding=utf-8
from __future__ import unicode_literals

from datetime import date
from django.core.urlresolvers import reverse

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible

from slugify import slugify
from taggit.managers import TaggableManager
from taggit.models import TagBase, GenericTaggedItemBase


class PostTag(TagBase):
    class Meta:
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')

    def slugify(self, tag, i=None):
        slug = slugify(tag)
        if i is not None:
            slug += '-%d' % i
        return slug


class PostTaggedItem(GenericTaggedItemBase):
    tag = models.ForeignKey(PostTag, related_name="%(app_label)s_%(class)s_items")


@python_2_unicode_compatible
class Post(models.Model):
    title = models.CharField('Заголовок', max_length=700)
    body = models.TextField('Контент', blank=True)
    slug = models.SlugField('Слаг', max_length=70, help_text='URL', unique=True)
    date = models.DateField('Дата публикации', default=date.today())

    tags = TaggableManager(through=PostTaggedItem)

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('content:post_view', args=[self.slug])

