# Generated by Django 2.1 on 2018-08-17 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companyManagment', '0016_auto_20180817_0757'),
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