# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models
import django_boto.s3.storage


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=b'30')),
                ('slug', models.SlugField(max_length=b'35')),
                ('logo', models.ImageField(storage=django_boto.s3.storage.S3Storage(), upload_to=b'game-logos/', blank=True)),
                ('source', models.FileField(storage=django_boto.s3.storage.S3Storage(), upload_to=b'game-source/', blank=True)),
                ('description', tinymce.models.HTMLField(blank=True)),
                ('publish_date', models.DateField()),
                ('status', models.BooleanField(default=False, verbose_name=b'Active')),
                ('is_editor', models.BooleanField(default=False, verbose_name=b"Editor's Choice")),
                ('is_special', models.BooleanField(default=False, verbose_name=b'Special')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=b'30')),
                ('genre_content', tinymce.models.HTMLField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='game',
            name='genre',
            field=models.ManyToManyField(to='game.Genre'),
            preserve_default=True,
        ),
    ]
