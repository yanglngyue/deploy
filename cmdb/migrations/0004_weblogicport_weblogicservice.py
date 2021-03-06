# Generated by Django 2.2.5 on 2019-11-23 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0003_auto_20191106_1910'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeblogicPort',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('port', models.IntegerField(blank=True, null=True, verbose_name='应用端口')),
            ],
        ),
        migrations.CreateModel(
            name='WeblogicService',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('service_name', models.CharField(max_length=64, unique=True, verbose_name='应用名')),
            ],
        ),
    ]
