from django.contrib import admin
from .models import Sku, SkuData


# Sku data Admin
class SkuDataAdminInline(admin.TabularInline):
    model = SkuData
    readonly_fields = ('sales_total',)


# Sku Admin
class SkuAdmin(admin.ModelAdmin):
    inlines = (SkuDataAdminInline,)
    fields = ('sku', 'total_units', 'sku_description',)


admin.site.register(Sku, SkuAdmin)
