import random  # define the random module
import string
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.contrib.sessions.models import Session
from django.contrib import admin
from .models import *
from .forms import AppUserForm
from django.utils.html import format_html
from django.urls import path, include
from django.shortcuts import render
from django import forms
import openpyxl
import pylightxl as xl
from cms.models import Group as G
import random
from django.http import HttpResponse
from datetime import datetime
import xlwt
# Register your models here.

# admin.site.register(Try)
from django.contrib.auth.models import User


admin.site.unregister(User)


# class AppUserResource(resources.ModelResource):
#     class Meta:
#         model = AppUser

class ImportCsvForm(forms.Form):
    import_Excel = forms.FileField()


@admin.register(AppUser)
class AppUserAdmin(admin.ModelAdmin):
    form = AppUserForm
    list_display = ['id', 'username', 'first_name',
                    'last_name', 'email', 'contact_no', 'active']
    readonly_fields = ['created_by', 'updated_by']
    search_fields = ['username']

    def save_model(self, request, obj, form, change):
        if obj.created_by == None:
            obj.created_by = request.user
        else:
            obj.updated_by = request.user
        super().save_model(request, obj, form, change)

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('import_csv/', self.import_csv),
            path('to_excel/', self.to_excel),
        ]
        return my_urls + urls

    def import_csv(self, request):
        form = ImportCsvForm
        if request.method == 'POST':
            excel = request.FILES['import_Excel']
            wb = xl.readxl(excel)
            name = wb.ws_names
            sheet = wb.ws('Sheet1')
            print(sheet.rows)
            for r in sheet.rows:
                print(r)
            for row in sheet.rows:
                print(row[0])
                if row[0] == 'ID':
                    pass
                else:
                    username = int(row[0])
                    first_name = row[1]
                    last_name = row[2]
                    email = row[3]
                    contact_no = str(row[4])
                    try:
                        if contact_no[-2] == '.':
                            contact_no = contact_no[:-2]
                    except:
                        pass
                    password = self.generate_random()
                    groups = row[5].split(',')
                    all_gps = []
                    for g in groups:
                        if g[0] == ' ':
                            g = g[1:]
                            print(g)
                        try:
                            gp = G.objects.get(name=g)
                            all_gps.append(gp)
                        except:
                            pass
                    try:
                        appuser = AppUser.objects.create(
                            username=str(username), password=password, email=email, first_name=first_name, last_name=last_name, contact_no=contact_no)
                        for gp in all_gps:
                            appuser.groups.add(gp)
                        appuser.save()
                    except:
                        pass
        context = {'form': form}
        return render(request, "admin/import_csv.html", context)

    def generate_random(self):
        S = 10
        ran = ''.join(random.choices(string.ascii_letters +
                                     string.digits, k=S))
        return ran

    def to_excel(self, request):
        response = HttpResponse(content_type='appplication/ms-excel')
        response['Content-Disposition'] = 'attachment; filename=Appuser.xls'
        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Sheet1')
        row_num = 0
        font_style = xlwt.XFStyle()
        font_style.font.bold = True
        columns = ['ID', 'First name', 'Last name',
                   'Email', 'Contact No', 'Groups']
        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)
        font_style = xlwt.XFStyle()
        rows = AppUser.objects.all()
        for row in rows:
            row_num += 1
            gp = row.groups.all()
            group = ''
            for g in gp:
                group = group+g.name+','
            group = group[:-1]
            # for col_num in range(len(row)):
            ws.write(row_num, 0, row.username, font_style)
            ws.write(row_num, 1, row.first_name, font_style)
            ws.write(row_num, 2, row.last_name, font_style)
            ws.write(row_num, 3, row.email, font_style)
            ws.write(row_num, 4, row.contact_no, font_style)
            ws.write(row_num, 5, group, font_style)

        wb.save(response)

        return response
