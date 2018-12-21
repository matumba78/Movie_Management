# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('artist', models.CharField(default=b'None', max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Artists',
            },
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('director', models.CharField(default=b'None', max_length=50)),
            ],
            options={
                'verbose_name_plural': 'director',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('genre', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name_plural': 'gener',
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('movie_name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('production_house', models.CharField(default=b'None', max_length=100)),
                ('rating', models.DecimalField(default=1, max_digits=2, decimal_places=1)),
                ('date', models.DateField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='genre',
            name='movie',
            field=models.ManyToManyField(to='Movie.Movie'),
        ),
        migrations.AddField(
            model_name='artist',
            name='movie',
            field=models.ManyToManyField(to='Movie.Movie'),
        ),
    ]
