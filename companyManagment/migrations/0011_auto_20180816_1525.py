# Generated by Django 2.1 on 2018-08-16 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companyManagment', '0010_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addcompanyadmin',
            name='admin',
        ),
        migrations.RemoveField(
            model_name='addcompanyadmin',
            name='company',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='company',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='AddCompanies',
        ),
        migrations.DeleteModel(
            name='AddCompanyAdmin',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
