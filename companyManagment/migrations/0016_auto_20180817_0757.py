# Generated by Django 2.1 on 2018-08-17 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companyManagment', '0015_invitation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitation',
            name='status',
            field=models.CharField(default='', max_length=50),
        ),
    ]
