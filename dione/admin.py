from django.contrib import admin
from dione.models import Company, Employee


# Register your models here.

class EmployeeInline(admin.TabularInline):
    model = Employee


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'email', 'employer')
    list_filter = ('employer',)


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')

    inlines = [EmployeeInline]


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Company, CompanyAdmin)
