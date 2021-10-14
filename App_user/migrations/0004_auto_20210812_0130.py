# Generated by Django 3.2.6 on 2021-08-11 19:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('App_user', '0003_appuser_groups'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='active',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
