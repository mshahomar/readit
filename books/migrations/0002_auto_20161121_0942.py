# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(help_text='Use pen name, not real name', unique=True, max_length=70)),
            ],
        ),
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.AlterField(
            model_name='book',
            name='is_favourite',
            field=models.BooleanField(verbose_name='Favourite?', default=False),
        ),
        migrations.AddField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(related_name='books', to='books.Author'),
        ),
    ]
