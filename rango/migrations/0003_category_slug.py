# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_auto_20150524_0254'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=datetime.date(2015, 5, 25), unique=True),
            preserve_default=False,
        ),
    ]
