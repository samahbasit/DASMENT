# Generated by Django 3.1.2 on 2020-11-03 06:19

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0004_auto_20201103_0612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='environmental',
            name='user',
            field=models.CharField(default='None', max_length=100, verbose_name=django.contrib.auth.models.User),
        ),
    ]