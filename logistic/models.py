from django.db import models
from common.models import Factory, CropYear
from farmer.models import Farmer, Village


class Car(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name="نام ماشین")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "ماشین"
        verbose_name_plural = "ماشین‌ها"


class Driver(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name="نام")
    last_name = models.CharField(max_length=255, verbose_name="نام خانوادگی")
    national_code = models.CharField(max_length=10, verbose_name="کد ملی")
    phone_number = models.CharField(max_length=11, verbose_name="شماره تماس")
    car = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True, related_name='drivers', verbose_name="ماشین")
    license_plate = models.CharField(max_length=255, verbose_name="پلاک")
    capacity_ton = models.DecimalField(max_digits=12, decimal_places=4, verbose_name="ظرفیت (تن)")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "راننده"
        verbose_name_plural = "راننده‌ها"


class Carriage(models.Model):
    id = models.BigAutoField(primary_key=True)
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE, related_name='carriages', verbose_name="کشاورز")
    village = models.ForeignKey(Village, on_delete=models.SET_NULL, null=True, related_name='carriages', verbose_name="روستا")
    crop_year = models.ForeignKey(CropYear, on_delete=models.CASCADE, related_name='carriages', verbose_name="سال زراعی")
    loading_date = models.CharField(max_length=10, verbose_name="تاریخ بارگیری")
    weight = models.DecimalField(max_digits=12, decimal_places=4, verbose_name="وزن محموله")
    origin_id = models.BigIntegerField(verbose_name="شناسه مبدا")
    destination_id = models.BigIntegerField(verbose_name="شناسه مقصد")
    carriage_fee_per_ton = models.DecimalField(max_digits=12, decimal_places=4, verbose_name="هزینه حمل به ازای تن")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "حمل و نقل"
        verbose_name_plural = "حمل و نقل‌ها"
        db_table = 'carriage'

    def __str__(self):
        return f"حمل و نقل ID: {self.id}"


class CarriageStatus(models.Model):
    id = models.BigAutoField(primary_key=True)
    carriage = models.ForeignKey(Carriage, on_delete=models.CASCADE, related_name='statuses', verbose_name="حمل و نقل")
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True, related_name='carriage_statuses',
                               verbose_name="راننده")
    carriage_status = models.CharField(max_length=255, verbose_name="وضعیت")
    carried = models.BooleanField(default=False, verbose_name="حمل شده؟")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "وضعیت حمل و نقل"
        verbose_name_plural = "وضعیت‌های حمل و نقل"

class BulkSmsJob(models.Model):
    id = models.BigAutoField(primary_key=True)
    job_id = models.CharField(max_length=36, verbose_name="شناسه کار")
    status = models.CharField(max_length=20, verbose_name="وضعیت")
    pattern_code = models.CharField(max_length=50, verbose_name="کد الگو")
    total_farmers = models.IntegerField(verbose_name="کل کشاورزان")
    processed_farmers = models.IntegerField(verbose_name="پردازش شده")
    succeeded_farmers = models.IntegerField(verbose_name="موفق")
    failed_farmers = models.IntegerField(verbose_name="ناموفق")
    completed_at = models.DateTimeField(null=True, blank=True, verbose_name="تاریخ اتمام")
    farmer_ids = models.JSONField(null=True, blank=True, verbose_name="شناسه‌های کشاورزان (همه)")
    succeeded_farmer_ids = models.JSONField(null=True, blank=True, verbose_name="شناسه‌های موفق")
    failed_farmer_ids = models.JSONField(null=True, blank=True, verbose_name="شناسه‌های ناموفق")
    failed_sms_details = models.JSONField(null=True, blank=True, verbose_name="جزئیات خطای پیامک")
    config_json = models.JSONField(null=True, blank=True, verbose_name="تنظیمات پیکربندی")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "عملیات پیامک انبوه"
        verbose_name_plural = "عملیات‌های پیامک انبوه"

    def __str__(self):
        return f"Job ID: {self.job_id} ({self.status})"


class FarmersLoad(models.Model):
    id = models.BigAutoField(primary_key=True)

    farmer = models.ForeignKey(
        Farmer,
        on_delete=models.CASCADE,
        related_name='loads',
        verbose_name="کشاورز"
    )
    factory = models.ForeignKey(
        Factory,
        on_delete=models.CASCADE,
        related_name='loads',
        verbose_name="کارخانه"
    )
    crop_year = models.ForeignKey(
        CropYear,
        on_delete=models.CASCADE,
        related_name='farmers_loads',
        verbose_name="سال زراعی"
    )
    date = models.CharField(max_length=10, verbose_name="تاریخ بارگیری")
    load_number = models.CharField(max_length=50, verbose_name="شماره بار")
    driver_name = models.CharField(max_length=255, verbose_name="نام راننده")
    phone_number = models.CharField(max_length=15, verbose_name="شماره تلفن راننده")
    total_weight = models.DecimalField(max_digits=12, decimal_places=4, verbose_name="وزن کل (تناژ)")
    dirt_weight = models.DecimalField(max_digits=12, decimal_places=4, verbose_name="وزن ناخالصی (خاک)")
    pest_weight = models.DecimalField(max_digits=12, decimal_places=4, verbose_name="وزن ناخالصی (آفت)")
    pure_weight = models.DecimalField(max_digits=12, decimal_places=4, verbose_name="وزن خالص")
    sugar_beet_polarity = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="خلوص (پولاریزاسیون) چغندر")
    price_per_kilo = models.DecimalField(max_digits=12, decimal_places=4, verbose_name="قیمت بر کیلو")
    rent_help = models.DecimalField(max_digits=12, decimal_places=4, verbose_name="کمک هزینه کرایه")
    transportation_cost = models.DecimalField(max_digits=12, decimal_places=4, verbose_name="هزینه حمل و نقل")
    quota_sugar_price = models.DecimalField(max_digits=12, decimal_places=4, verbose_name="قیمت سهمیه شکر")
    quota_pulp_price = models.DecimalField(max_digits=12, decimal_places=4, verbose_name="قیمت سهمیه تفاله")
    pure_payable = models.DecimalField(max_digits=12, decimal_places=4, verbose_name="خالص قابل پرداخت")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "بارگیری کشاورز"
        verbose_name_plural = "بارگیری کشاورزان"
        db_table = 'farmers_load'

    def __str__(self):
        return f"بار شماره {self.load_number} از کشاورز {self.farmer_id}"

class FactoryCommitmentTonnage(models.Model):
    id = models.BigAutoField(primary_key=True)
    factory = models.ForeignKey(Factory, on_delete=models.CASCADE, related_name='commitment_tonnages', verbose_name="کارخانه")
    crop_year = models.ForeignKey(CropYear, on_delete=models.CASCADE, related_name='factory_commitment_tonnages', verbose_name="سال زراعی")
    committed_tonnage_amount = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        verbose_name="مقدار تناژ تعهد شده"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "تعهد تناژ کارخانه"
        verbose_name_plural = "تعهدات تناژ کارخانه"
        db_table = 'factory_commitment_tonnage'


    def __str__(self):
        return f"تعهد تناژ برای Factory ID: {self.factory_id} در سال {self.crop_year_id}"