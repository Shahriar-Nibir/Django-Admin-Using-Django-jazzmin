from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User


class Account(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self) -> str:
        return self.name


class SessionDetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=300, null=True)
    remote_ip = models.CharField(max_length=300, null=True)
    user_agent = models.CharField(max_length=300, null=True)
    device_family = models.CharField(max_length=300, null=True)
    # device_brand = models.CharField(max_length=300, null=True)
    # device_model = models.CharField(max_length=300, null=True)
    remote_ip_country = models.CharField(max_length=300, null=True)
    browser = models.CharField(max_length=300, null=True)
    os = models.CharField(max_length=300, null=True)
    browser_version = models.CharField(max_length=300, null=True)
    os_version = models.CharField(max_length=300, null=True)
    login_time = models.DateTimeField(null=True, blank=True)
    logout_time = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(null=True)


class Staff(models.Model):
    account = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    username = models.CharField(max_length=200, null=True)
    password = models.CharField(max_length=200, null=True, blank=True)
    confirm_password = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    contact_no = models.CharField(max_length=20, null=True, blank=-True)
    # profile_pic = models.ImageField(null=True, blank=True)
    active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        user = self.account
        password = self.password
        email = self.email
        if password is None:
            pass
        else:
            user.set_password(password)
        user.email = email
        user.is_active = self.active
        user.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username
