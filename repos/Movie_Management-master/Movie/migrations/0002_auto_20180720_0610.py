# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Movie', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.ForeignKey(blank=True, to='Movie.Director', null=True),
        ),
        migrations.AlterField(
            model_name='director',
            name='director',
            field=models.CharField(default=b'None', unique=True, max_length=50),
        ),
    ]
