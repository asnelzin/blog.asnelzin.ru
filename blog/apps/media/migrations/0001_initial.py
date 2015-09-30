# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('image', models.ImageField(upload_to='images/%Y/%m/%d', verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Media',
                'verbose_name_plural': 'Media',
            },
            bases=(models.Model,),
        ),
    ]
