# Generated by Django 2.1 on 2018-08-17 09:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companyManagment', '0019_invitation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitation',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]