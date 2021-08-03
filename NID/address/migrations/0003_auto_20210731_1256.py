# Generated by Django 3.0.8 on 2021-07-31 12:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0002_auto_20210731_1043'),
    ]

    operations = [
        migrations.AddField(
            model_name='localbody',
            name='num_wards',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(1)]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='district',
            name='id',
            field=models.PositiveIntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='localbody',
            name='id',
            field=models.PositiveIntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='localbodycategory',
            name='id',
            field=models.PositiveIntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='region',
            name='id',
            field=models.PositiveIntegerField(primary_key=True, serialize=False),
        ),
    ]