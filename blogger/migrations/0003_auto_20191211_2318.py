# Generated by Django 2.2.6 on 2019-12-11 17:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogger', '0002_auto_20191117_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogger',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
