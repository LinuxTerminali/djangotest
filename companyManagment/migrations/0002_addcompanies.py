# Generated by Django 2.1 on 2018-08-16 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companyManagment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddCompanies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('description', models.TextField()),
            ],
        ),
    ]