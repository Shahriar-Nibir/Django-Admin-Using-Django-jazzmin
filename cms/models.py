from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User
from system.models import Account


class Group(models.Model):
    name = models.CharField(max_length=200, null=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    created_by = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.DO_NOTHING, related_name='group_created_by')
    updated_by = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.DO_NOTHING, related_name='group_updated_by')

    def __str__(self):
        return self.name


class Page(models.Model):
    name = models.CharField(max_length=200, null=True)
    content = models.TextField(null=True)
    groups = models.ManyToManyField(Group, blank=True)
    is_homepage = models.BooleanField(blank=True)
    created_by = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.DO_NOTHING, related_name='page_created_by')
    updated_by = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.DO_NOTHING, related_name='page_updated_by')

    def __str__(self):
        return self.name
