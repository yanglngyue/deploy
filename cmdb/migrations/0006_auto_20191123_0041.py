# Generated by Django 2.2.5 on 2019-11-23 00:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0005_weblogicservice_weblogic_service_port'),
    ]

    operations = [
        migrations.RenameField(
            model_name='weblogicservice',
            old_name='service_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='weblogicservice',
            old_name='weblogic_service_port',
            new_name='weblogicport',
        ),
    ]
