# Generated by Django 2.1 on 2018-08-16 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companyManagment', '0003_addcompanyadmin'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='company',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='companyManagment.AddCompanies'),
            preserve_default=False,
        ),
    ]
