# Generated by Django 2.1 on 2018-08-16 15:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('companyManagment', '0011_auto_20180816_1525'),
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
        migrations.CreateModel(
            name='AddCompanyAdmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('company', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='companyManagment.AddCompanies')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin', models.BooleanField(default=False)),
                ('description', models.CharField(default='', max_length=100)),
                ('city', models.CharField(default='', max_length=100)),
                ('website', models.URLField(default='')),
                ('phone', models.IntegerField(default=0)),
                ('image', models.ImageField(blank=True, upload_to='profile_image')),
                ('company', models.OneToOneField(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='companyManagment.AddCompanies')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            managers=[
                ('london', django.db.models.manager.Manager()),
            ],
        ),
    ]
