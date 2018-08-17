# Generated by Django 2.1 on 2018-08-17 10:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('companyManagment', '0025_auto_20180817_0947'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invitation',
            name='invitedby',
        ),
        migrations.AddField(
            model_name='invitation',
            name='invitedby',
            field=models.ManyToManyField(default=17, related_name='invitedby', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='invitation',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]