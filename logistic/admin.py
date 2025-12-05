from django.contrib import admin
from .models import (
    Car, Driver, Carriage, CarriageStatus, BulkSmsJob, FarmersLoad, FactoryCommitmentTonnage
)


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)
    ordering = ('name',)


class DriverInline(admin.TabularInline):
    model = Driver
    extra = 0
    fields = ('name', 'last_name', 'national_code', 'phone_number', 'license_plate', 'capacity_ton')
    readonly_fields = ('created_at',)


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'national_code', 'phone_number', 'car', 'license_plate', 'capacity_ton')
    list_filter = ('car',)
    search_fields = ('name', 'last_name', 'national_code', 'license_plate')
    raw_id_fields = ('car',)


class CarriageStatusInline(admin.TabularInline):
    model = CarriageStatus
    extra = 0
    fields = ('driver', 'carriage_status', 'carried', 'created_at')
    readonly_fields = ('created_at',)
    raw_id_fields = ('driver',)


@admin.register(Carriage)
class CarriageAdmin(admin.ModelAdmin):
    list_display = ('farmer', 'crop_year', 'village', 'loading_date', 'weight', 'carriage_fee_per_ton')
    list_filter = ('crop_year', 'village__city')
    search_fields = ('farmer__full_name', 'village__village_name')
    raw_id_fields = ('farmer', 'village', 'crop_year')
    inlines = [CarriageStatusInline]


@admin.register(CarriageStatus)
class CarriageStatusAdmin(admin.ModelAdmin):
    list_display = ('carriage', 'driver', 'carriage_status', 'carried', 'created_at')
    list_filter = ('carriage_status', 'carried')
    search_fields = ('carriage__farmer__full_name', 'driver__name', 'carriage_status')
    raw_id_fields = ('carriage', 'driver')


@admin.register(FarmersLoad)
class FarmersLoadAdmin(admin.ModelAdmin):
    list_display = (
        'load_number', 'farmer', 'factory', 'date', 'pure_weight',
        'sugar_beet_polarity', 'pure_payable'
    )
    list_filter = ('crop_year', 'factory')
    search_fields = ('load_number', 'farmer__full_name', 'driver_name')
    ordering = ('-date', '-created_at')
    fieldsets = (
        (None, {'fields': ('farmer', 'factory', 'crop_year', 'date', 'load_number', 'driver_name', 'phone_number')}),
        ('جزئیات وزن و کیفیت',
         {'fields': ('total_weight', 'dirt_weight', 'pest_weight', 'pure_weight', 'sugar_beet_polarity')}),
        ('محاسبات مالی', {'fields': (
        'price_per_kilo', 'rent_help', 'transportation_cost', 'quota_sugar_price', 'quota_pulp_price',
        'pure_payable')}),
    )
    raw_id_fields = ('farmer', 'factory', 'crop_year')


@admin.register(FactoryCommitmentTonnage)
class FactoryCommitmentTonnageAdmin(admin.ModelAdmin):
    list_display = ('factory', 'crop_year', 'committed_tonnage_amount', 'created_at')
    list_filter = ('crop_year', 'factory')
    search_fields = ('factory__factory_name',)
    raw_id_fields = ('factory', 'crop_year')


@admin.register(BulkSmsJob)
class BulkSmsJobAdmin(admin.ModelAdmin):
    list_display = ('job_id', 'status', 'total_farmers', 'succeeded_farmers', 'failed_farmers', 'completed_at')
    list_filter = ('status',)
    search_fields = ('job_id', 'pattern_code')
    readonly_fields = ('farmer_ids', 'succeeded_farmer_ids', 'failed_farmer_ids', 'failed_sms_details', 'config_json')
    ordering = ('-created_at',)