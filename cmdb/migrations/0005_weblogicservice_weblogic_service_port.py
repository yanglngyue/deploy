# Generated by Django 2.2.5 on 2019-11-23 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0004_weblogicport_weblogicservice'),
    ]

    operations = [
        migrations.AddField(
            model_name='weblogicservice',
            name='weblogic_service_port',
            field=models.ManyToManyField(to='cmdb.WeblogicPort'),
        ),
    ]
