# Generated by Django 3.2.6 on 2021-08-13 18:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('system', '0003_alter_staff_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='user',
        ),
        migrations.AddField(
            model_name='staff',
            name='account',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='staff',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='email',
            field=models.EmailField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='first_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='last_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='password1',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='password2',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='staff',
            name='username',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='contact_no',
            field=models.CharField(blank=-1, max_length=20, null=True),
        ),
    ]
