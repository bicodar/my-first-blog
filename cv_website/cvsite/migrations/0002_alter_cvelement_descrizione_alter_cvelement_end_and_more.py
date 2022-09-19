# Generated by Django 4.1.1 on 2022-09-19 14:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cvsite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cvelement',
            name='descrizione',
            field=models.CharField(default=None, max_length=60),
        ),
        migrations.AlterField(
            model_name='cvelement',
            name='end',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='cvelement',
            name='nome',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='cvelement',
            name='riassunto',
            field=models.CharField(default=None, max_length=500),
        ),
        migrations.AlterField(
            model_name='cvelement',
            name='start',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
    ]
