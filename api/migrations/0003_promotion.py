# Generated by Django 2.2.5 on 2019-11-01 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=1024, null=True, verbose_name='版本名称')),
                ('select', models.CharField(blank=True, max_length=1024, null=True, verbose_name='升级类型')),
                ('extent', models.CharField(blank=True, max_length=1024, null=True, verbose_name='升级范围')),
                ('info', models.CharField(blank=True, max_length=1024, null=True, verbose_name='升级内容')),
                ('uptime', models.DateTimeField(auto_now_add=True, null=True, verbose_name='升级时间')),
                ('ps', models.CharField(blank=True, max_length=1024, null=True, verbose_name='备注')),
            ],
        ),
    ]
