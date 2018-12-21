# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Movie', '0002_auto_20180720_0610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='director',
            name='director',
            field=models.CharField(default=b'None', max_length=50),
        ),
    ]
