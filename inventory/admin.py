from django.contrib import admin
from .models import (
    Seed, Pesticide, FactorySeed, FactoryPesticide,
    FarmersSeed, FarmersPesticide, FactorySugar, FactoryWaste,
    FarmersSugarDelivery, FarmersWasteDelivery
)

@admin.register(Seed)
class SeedAdmin(admin.ModelAdmin):
    list_display = ('seed_name', 'measure_unit', 'created_at')
    search_fields = ('seed_name',)
    ordering = ('seed_name',)
    raw_id_fields = ('measure_unit',)

@admin.register(Pesticide)
class PesticideAdmin(admin.ModelAdmin):
    list_display = ('pesticide_name', 'measure_unit', 'created_at')
    search_fields = ('pesticide_name',)
    ordering = ('pesticide_name',)
    raw_id_fields = ('measure_unit',)


@admin.register(FactorySeed)
class FactorySeedAdmin(admin.ModelAdmin):
    list_display = ('factory', 'seed', 'crop_year', 'amount', 'farmer_price', 'factory_price')
    list_filter = ('crop_year', 'factory', 'seed')
    search_fields = ('factory__factory_name', 'seed__seed_name')
    raw_id_fields = ('factory', 'seed', 'crop_year')

@admin.register(FactoryPesticide)
class FactoryPesticideAdmin(admin.ModelAdmin):
    list_display = ('factory', 'pesticide', 'crop_year', 'amount', 'farmer_price', 'factory_price')
    list_filter = ('crop_year', 'factory', 'pesticide')
    search_fields = ('factory__factory_name', 'pesticide__pesticide_name')
    raw_id_fields = ('factory', 'pesticide', 'crop_year')

@admin.register(FactorySugar)
class FactorySugarAdmin(admin.ModelAdmin):
    list_display = ('factory', 'crop_year', 'sugar_weight_received_factory', 'sugar_price_received_factory')
    list_filter = ('crop_year', 'factory')
    search_fields = ('factory__factory_name',)
    raw_id_fields = ('factory', 'crop_year')

@admin.register(FactoryWaste)
class FactoryWasteAdmin(admin.ModelAdmin):
    list_display = ('factory', 'crop_year', 'waste_weight_received_factory', 'waste_price_received_factory')
    list_filter = ('crop_year', 'factory')
    search_fields = ('factory__factory_name',)
    raw_id_fields = ('factory', 'crop_year')


@admin.register(FarmersSeed)
class FarmersSeedAdmin(admin.ModelAdmin):
    list_display = ('commitment', 'seed', 'factory', 'seed_amount', 'price', 'price_for_all_farmers_check')
    list_filter = ('crop_year', 'factory', 'price_for_all_farmers_check')
    search_fields = ('commitment__farmer__full_name', 'seed__seed_name')
    raw_id_fields = ('commitment', 'seed', 'factory', 'crop_year')

@admin.register(FarmersPesticide)
class FarmersPesticideAdmin(admin.ModelAdmin):
    list_display = ('commitment', 'pesticide', 'factory', 'pesticide_amount', 'price', 'price_for_all_farmers_check')
    list_filter = ('crop_year', 'factory', 'price_for_all_farmers_check')
    search_fields = ('commitment__farmer__full_name', 'pesticide__pesticide_name')
    raw_id_fields = ('commitment', 'pesticide', 'factory', 'crop_year')


@admin.register(FarmersSugarDelivery)
class FarmersSugarDeliveryAdmin(admin.ModelAdmin):
    list_display = ('farmer', 'crop_year', 'sugar_delivered', 'sugar_deposit_amount', 'created_at')
    list_filter = ('crop_year',)
    search_fields = ('farmer__full_name',)
    raw_id_fields = ('farmer', 'crop_year')

@admin.register(FarmersWasteDelivery)
class FarmersWasteDeliveryAdmin(admin.ModelAdmin):
    list_display = ('farmer', 'crop_year', 'waste_delivered', 'waste_deposit_amount', 'created_at')
    list_filter = ('crop_year',)
    search_fields = ('farmer__full_name',)
    raw_id_fields = ('farmer', 'crop_year')