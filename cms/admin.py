from django.contrib import admin
from .models import *
# Register your models here.


class GroupAdmin(admin.ModelAdmin):
    model = Group
    list_display = ['id', 'name']
    readonly_fields = ['created_by', 'updated_by']
    search_fields = ['name']

    def save_model(self, request, obj, form, change):
        if obj.created_by == None:
            obj.created_by = request.user
        else:
            obj.updated_by = request.user
        super().save_model(request, obj, form, change)


class PageAdmin(admin.ModelAdmin):
    model = Page
    list_display = ['id', 'name']
    readonly_fields = ['created_by', 'updated_by']
    search_fields = ['name']

    def save_model(self, request, obj, form, change):
        if obj.created_by == None:
            obj.created_by = request.user
        else:
            obj.updated_by = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Group, GroupAdmin)
admin.site.register(Page, PageAdmin)
