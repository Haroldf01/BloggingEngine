# Generated by Django 2.2.6 on 2019-11-17 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogger', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogger',
            old_name='auther',
            new_name='author',
        ),
        migrations.AlterField(
            model_name='blogger',
            name='img',
            field=models.ImageField(upload_to='C:\\Users\\Arsalaan\\PycharmProjects\\portfolio_reactify\\blogger/media'),
        ),
    ]
