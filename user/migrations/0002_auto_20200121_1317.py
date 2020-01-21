# Generated by Django 2.2.6 on 2020-01-21 13:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message='phone number must be entered with country code & without spaces.', regex='^\\+?1?\\d{9,14}$')]),
        ),
    ]
