# Generated by Django 2.2.5 on 2019-11-19 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_partment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='detail',
        ),
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.RemoveField(
            model_name='book',
            name='publisher',
        ),
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.FileField(default='avatars/default.png', upload_to='avatars/', verbose_name='头像'),
        ),
    ]
