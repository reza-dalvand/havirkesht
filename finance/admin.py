from django.contrib import admin
from .models import (
    PurityPrice, ProductPrice, FarmersPayment, FarmersInvoicePayed,
    FarmersGuarantee, FactoryPayment
)


@admin.register(PurityPrice)
class PurityPriceAdmin(admin.ModelAdmin):
    list_display = ('crop_year', 'base_purity', 'base_purity_price', 'price_difference', 'updated_at')
    list_filter = ('crop_year',)
    search_fields = ('crop_year__crop_year_name',)
    ordering = ('-crop_year', 'base_purity')
    raw_id_fields = ('crop_year',)

@admin.register(ProductPrice)
class ProductPriceAdmin(admin.ModelAdmin):
    list_display = ('crop_year', 'sugar_price_per_kg', 'pulp_price_per_kg', 'updated_at')
    list_filter = ('crop_year',)
    search_fields = ('crop_year__crop_year_name',)
    raw_id_fields = ('crop_year',)


@admin.register(FarmersPayment)
class FarmersPaymentAdmin(admin.ModelAdmin):
    list_display = ('farmer', 'crop_year', 'payment_type', 'price', 'created_at')
    list_filter = ('crop_year', 'payment_type')
    search_fields = ('farmer__full_name', 'payment_type__reason_name')
    ordering = ('-created_at',)
    raw_id_fields = ('farmer', 'crop_year', 'payment_type')

@admin.register(FarmersInvoicePayed)
class FarmersInvoicePayedAdmin(admin.ModelAdmin):
    list_display = ('farmer', 'crop_year', 'payed', 'updated_at')
    list_filter = ('crop_year', 'payed')
    search_fields = ('farmer__full_name',)
    list_editable = ('payed',)
    raw_id_fields = ('farmer', 'crop_year')

@admin.register(FarmersGuarantee)
class FarmersGuaranteeAdmin(admin.ModelAdmin):
    list_display = ('guarantor_farmer', 'guaranteed_farmer', 'guarantee_price', 'crop_year')
    list_filter = ('crop_year',)
    search_fields = ('guarantor_farmer__full_name', 'guaranteed_farmer__full_name')
    raw_id_fields = ('guarantor_farmer', 'guaranteed_farmer', 'crop_year')


@admin.register(FactoryPayment)
class FactoryPaymentAdmin(admin.ModelAdmin):
    list_display = ('title', 'factory', 'crop_year', 'price', 'date', 'user')
    list_filter = ('crop_year', 'factory')
    search_fields = ('title', 'factory__factory_name', 'user__fullname')
    date_hierarchy = 'date'
    raw_id_fields = ('user', 'crop_year', 'factory')