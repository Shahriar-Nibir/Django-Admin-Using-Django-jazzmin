from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User
from cms.models import Group
from system.models import Account
# from .views import get_user


class AppUser(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    account = models.ForeignKey(
        Account, null=True, on_delete=models.CASCADE, blank=True)
    username = models.CharField(max_length=200, null=True, unique=True)
    password = models.CharField(
        max_length=200, null=True, blank=True)
    confirm_password = models.CharField(
        max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True)
    groups = models.ManyToManyField(Group)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    contact_no = models.CharField(max_length=20, null=True, blank=-True)
    profile_pic = models.ImageField(null=True, blank=True, default='logo.png')
    active = models.BooleanField(default=True)
    created_by = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.DO_NOTHING, related_name='appuser_created_by')
    updated_by = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.DO_NOTHING, related_name='appuser_updated_by')

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        username = self.username
        password = self.password
        email = self.email
        users = User.objects.all()
        username_list = []
        user = self.user
        # by = get_user()
        # if self.created_by is None:
        #     self.created_by = by
        # else:
        #     self.updated_by = by
        if user is not None:
            user.email = email
            user.username = username
            if password is not None:
                user.set_password(password)
            user.is_active = self.active
            user.save()

        # for u in users:
        #     username_list.append(u.username)
        else:
            if username not in username_list:
                try:
                    user, created = User.objects.update_or_create(
                        username=username, password=password, email=email, is_active=self.active)
                    user.set_password(password)
                    user.save()
                    self.user = user
                except:
                    pass
        # else:
        #     user = User.objects.get(username=username)
        #     user.email = email
        #     user.save()

        super().save(*args, **kwargs)
