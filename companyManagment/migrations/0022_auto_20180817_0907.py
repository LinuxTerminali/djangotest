# Generated by Django 2.1 on 2018-08-17 09:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companyManagment', '0021_auto_20180817_0906'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invitation',
            name='user',
        ),
        migrations.DeleteModel(
            name='Invitation',
        ),
    ]
