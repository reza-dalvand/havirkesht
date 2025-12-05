from django.contrib import admin
from .models import (
    Province, City, Village, Farmer,
    Supervisor, Commitment
)

class CommitmentInline(admin.TabularInline):
    model = Commitment
    extra = 0
    fields = ('crop_year', 'village', 'commitment_number', 'amount_of_land', 'withdrawal_amount', 'user')
    readonly_fields = ('created_at',)
    raw_id_fields = ('crop_year', 'village', 'user')


@admin.register(Province)
class ProvinceAdmin(admin.ModelAdmin):
    list_display = ('province', 'created_at')
    search_fields = ('province',)
    ordering = ('province',)


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('city', 'province', 'created_at')
    list_filter = ('province',)
    search_fields = ('city', 'province__province')
    raw_id_fields = ('province',)


@admin.register(Village)
class VillageAdmin(admin.ModelAdmin):
    list_display = ('village_name', 'city', 'created_at')
    list_filter = ('city__province',)
    search_fields = ('village_name', 'city__city')
    raw_id_fields = ('city',)


@admin.register(Supervisor)
class SupervisorAdmin(admin.ModelAdmin):
    list_display = ('name', 'national_id', 'phone', 'degree', 'capacity', 'supervision_permit')
    search_fields = ('name', 'national_id', 'phone')
    ordering = ('name',)
    fieldsets = (
        (None, {'fields': ('name', 'national_id', 'degree', 'phone', 'address')}),
        ('اطلاعات مالی', {'fields': ('shaba_id', 'bank_name')}),
        ('اطلاعات نظارت', {'fields': ('capacity', 'supervision_permit', 'lat', 'lng')}),
    )

@admin.register(Farmer)
class FarmerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'national_id', 'father_name', 'phone_number', 'created_at')
    search_fields = ('full_name', 'national_id', 'phone_number')
    ordering = ('full_name',)

    fieldsets = (
        (None, {'fields': ('full_name', 'father_name', 'national_id', 'phone_number', 'address')}),
        ('اطلاعات بانکی', {'fields': ('sheba_number_1', 'sheba_number_2', 'card_number')}),
    )
    inlines = [CommitmentInline]


@admin.register(Commitment)
class CommitmentAdmin(admin.ModelAdmin):
    list_display = (
    'farmer', 'crop_year', 'village', 'commitment_number', 'amount_of_land', 'withdrawal_amount', 'user')
    list_filter = ('crop_year', 'village')
    search_fields = ('farmer__full_name', 'commitment_number')
    raw_id_fields = ('farmer', 'crop_year', 'village', 'user')