# Generated by Django 3.2.6 on 2021-08-13 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_user', '0005_auto_20210812_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
