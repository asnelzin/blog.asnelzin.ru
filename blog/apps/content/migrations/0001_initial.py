# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=700, verbose_name='Title')),
                ('body', models.TextField(verbose_name='Content', blank=True)),
                ('slug', models.SlugField(help_text='URL', unique=True, max_length=70, verbose_name='Slug')),
                ('date', models.DateField(default=datetime.date(2015, 9, 30), verbose_name='Publish date')),
            ],
            options={
                'verbose_name': 'Post',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PostTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100, verbose_name='Name')),
                ('slug', models.SlugField(unique=True, max_length=100, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PostTaggedItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('object_id', models.IntegerField(verbose_name='Object id', db_index=True)),
                ('content_type', models.ForeignKey(related_name='content_posttaggeditem_tagged_items', verbose_name='Content type', to='contenttypes.ContentType')),
                ('tag', models.ForeignKey(related_name='content_posttaggeditem_items', to='content.PostTag')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=taggit.managers.TaggableManager(to='content.PostTag', through='content.PostTaggedItem', help_text='A comma-separated list of tags.', verbose_name='Tags'),
            preserve_default=True,
        ),
    ]
