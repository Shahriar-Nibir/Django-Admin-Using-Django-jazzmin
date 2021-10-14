from django.contrib import admin
from django.contrib.sessions.models import Session
from .models import *
from .forms import *
from django.utils.html import format_html
# Register your models here.

from django.contrib.auth.models import Group
admin.site.unregister(Group)


class SessionDetailAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return False

    @admin.display
    def logout_user(self, obj):
        if obj.is_active == True:
            return format_html("<a href='/logout/%s'><i class='fas fa-user-slash' aria-hidden='true'></i></a>" % obj.id)
        else:
            pass

    logout_user.allow_tags = True
    readonly_fields = ['user', 'token', 'remote_ip', 'user_agent', 'device_family', 'remote_ip_country',
                       'browser', 'os', 'browser_version', 'os_version', 'login_time', 'logout_time', 'is_active']
    list_display = ['user', 'login_time',
                    'logout_time', 'is_active', 'logout_user']


admin.site.register(SessionDetail, SessionDetailAdmin)


class StaffAdmin(admin.ModelAdmin):
    form = StaffForm
    list_display = ['id', 'account', 'username']

    def delete_model(self, request, obj, form, change):
        user = self.account
        user.is_staff = False
        user.is_superuser = False
        user.save()
        super().delete_model(request, obj, form, change)


class SessionAdmin(admin.ModelAdmin):
    def _session_data(self, obj):
        return obj.get_decoded()
    list_display = ['session_key', '_session_data', 'expire_date']


admin.site.register(Session, SessionAdmin)

admin.site.register(Staff, StaffAdmin)
# admin.site.register(Account)
