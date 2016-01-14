# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('zip_code', models.CharField(max_length=7)),
                ('address', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateTimeField(verbose_name='created at:', default=datetime.datetime(2016, 1, 13, 18, 2, 29, 765744, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='zip_code',
            field=models.ForeignKey(to='doctors.Hospital'),
        ),
    ]
