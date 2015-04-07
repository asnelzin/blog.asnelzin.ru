# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=700, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('body', models.TextField(verbose_name='\u041a\u043e\u043d\u0442\u0435\u043d\u0442', blank=True)),
                ('slug', models.SlugField(help_text='URL', unique=True, max_length=70, verbose_name='\u0421\u043b\u0430\u0433')),
                ('date', models.DateField(default=datetime.date(2015, 4, 7), verbose_name='\u0414\u0430\u0442\u0430 \u043f\u0443\u0431\u043b\u0438\u043a\u0430\u0446\u0438\u0438')),
            ],
            options={
                'verbose_name': '\u043f\u043e\u0441\u0442',
                'verbose_name_plural': '\u043f\u043e\u0441\u0442\u044b',
            },
            bases=(models.Model,),
        ),
    ]
