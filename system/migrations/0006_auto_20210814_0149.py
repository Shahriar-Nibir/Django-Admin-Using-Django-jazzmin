# Generated by Django 3.2.6 on 2021-08-13 19:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0005_account'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staff',
            old_name='password1',
            new_name='confirm_password',
        ),
        migrations.RenameField(
            model_name='staff',
            old_name='password2',
            new_name='password',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='profile_pic',
        ),
    ]