# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RelatedResource1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='RelatedResource2',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('active', models.BooleanField(default=True)),
                ('related_resources_1', models.ManyToManyField(to='testproject.RelatedResource1')),
            ],
        ),
        migrations.CreateModel(
            name='TestResource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('related_resource_1', models.ForeignKey(to='testproject.RelatedResource1')),
                ('related_resource_2', models.OneToOneField(to='testproject.RelatedResource2')),
            ],
        ),
    ]
