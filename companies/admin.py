from django.contrib import admin

from companies.models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('updated_at', 'created_at', 'company_token', )
    readonly_fields = ('updated_at', 'created_at', )
