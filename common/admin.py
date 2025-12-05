from django.contrib import admin
from .models import (
    MeasureUnit, CropYear, PaymentReason, AlembicVersion,
    Factory, Product, Roles, Users, TokenBlacklist
)

@admin.register(MeasureUnit)
class MeasureUnitAdmin(admin.ModelAdmin):
    list_display = ('unit_name', 'created_at')
    search_fields = ('unit_name',)
    ordering = ('unit_name',)


@admin.register(CropYear)
class CropYearAdmin(admin.ModelAdmin):
    list_display = ('crop_year_name', 'created_at')
    search_fields = ('crop_year_name',)
    ordering = ('-crop_year_name',)


@admin.register(PaymentReason)
class PaymentReasonAdmin(admin.ModelAdmin):
    list_display = ('reason_name', 'created_at')
    search_fields = ('reason_name',)
    ordering = ('reason_name',)


@admin.register(Factory)
class FactoryAdmin(admin.ModelAdmin):
    list_display = ('factory_name', 'created_at')
    search_fields = ('factory_name',)
    ordering = ('factory_name',)


# 2. مدل‌های محصول (با Foreign Keys)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'measure_unit', 'crop_year', 'created_at')
    list_filter = ('crop_year', 'measure_unit')
    search_fields = ('product_name',)
    raw_id_fields = ('measure_unit', 'crop_year')


class UsersInline(admin.TabularInline):
    model = Users
    extra = 0
    fields = ('username', 'fullname', 'phone_number', 'disabled', 'created_at')
    readonly_fields = ('created_at',)
    exclude = ('password',)


@admin.register(Roles)
class RolesAdmin(admin.ModelAdmin):
    list_display = ('name_user_role', 'created_at')
    search_fields = ('name_user_role',)
    inlines = [UsersInline]


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('username', 'fullname', 'phone_number', 'email', 'role_id', 'disabled')
    list_filter = ('disabled', 'role_id')
    search_fields = ('username', 'fullname', 'phone_number')
    exclude = ('password',)
    raw_id_fields = ('role_id',)


@admin.register(AlembicVersion)
class AlembicVersionAdmin(admin.ModelAdmin):
    list_display = ('version_num',)
    search_fields = ('version_num',)


@admin.register(TokenBlacklist)
class TokenBlacklistAdmin(admin.ModelAdmin):
    list_display = ('token', 'blacklisted_at', 'created_at')
    search_fields = ('token',)