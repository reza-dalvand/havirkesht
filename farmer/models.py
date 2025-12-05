from django.db import models
from common.models import Users, CropYear

class Province(models.Model):
    id = models.BigAutoField(primary_key=True)
    province = models.CharField(max_length=255, verbose_name="نام استان")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "استان"
        verbose_name_plural = "استان‌ها"

    def __str__(self):
        return self.province


class City(models.Model):
    id = models.BigAutoField(primary_key=True)
    city = models.CharField(max_length=255, verbose_name="نام شهر")
    province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='cities', verbose_name="استان")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "شهر"
        verbose_name_plural = "شهرها"

    def __str__(self):
        return self.city


class Village(models.Model):
    id = models.BigAutoField(primary_key=True)
    village_name = models.CharField(max_length=255, verbose_name="نام روستا")
    city = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='villages', verbose_name="استان")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "روستا"
        verbose_name_plural = "روستاها"

    def __str__(self):
        return self.village_name


class Farmer(models.Model):
    id = models.BigAutoField(primary_key=True)
    national_id = models.CharField(max_length=50, unique=True, verbose_name="کد ملی")
    full_name = models.CharField(max_length=255, verbose_name="نام و نام خانوادگی")
    father_name = models.CharField(max_length=255, verbose_name="نام پدر")
    phone_number = models.CharField(max_length=50, verbose_name="شماره تماس")
    sheba_number_1 = models.CharField(max_length=50, blank=True, null=True, verbose_name="شماره شبا ۱")
    sheba_number_2 = models.CharField(max_length=50, blank=True, null=True, verbose_name="شماره شبا ۲")
    card_number = models.CharField(max_length=50, blank=True, null=True, verbose_name="شماره کارت")
    address = models.CharField(max_length=500, blank=True, null=True, verbose_name="آدرس")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "کشاورز"
        verbose_name_plural = "کشاورزان"

    def __str__(self):
        return self.full_name


class Supervisor(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name="نام ناظر")
    national_id = models.BigIntegerField(verbose_name="کد ملی")
    degree = models.CharField(max_length=255, verbose_name="مدرک تحصیلی")
    phone = models.BigIntegerField(verbose_name="شماره تماس")
    shaba_id = models.CharField(max_length=255, verbose_name="شماره شبا")
    bank_name = models.CharField(max_length=255, verbose_name="نام بانک")
    address = models.CharField(max_length=255, verbose_name="آدرس")
    capacity = models.IntegerField(verbose_name="ظرفیت سرکشی (تناژ)")
    supervision_permit = models.CharField(max_length=255, verbose_name="مجوز نظارت")
    lat = models.DecimalField(max_digits=12, decimal_places=4, verbose_name="عرض جغرافیایی")
    lng = models.DecimalField(max_digits=12, decimal_places=4, verbose_name="طول جغرافیایی")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "ناظر"
        verbose_name_plural = "ناظران"



class Commitment(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True, related_name='commitments_created',
                             verbose_name="کاربر ایجاد کننده")
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE, related_name='commitments', verbose_name="کشاورز")
    crop_year = models.ForeignKey(CropYear, on_delete=models.CASCADE, related_name='commitments',
                                  verbose_name="سال زراعی")
    village = models.ForeignKey(Village, on_delete=models.SET_NULL, null=True, related_name='commitments',
                                verbose_name="روستا")

    commitment_number = models.CharField(max_length=50, verbose_name="شماره تعهد")
    amount_of_land = models.DecimalField(max_digits=12, decimal_places=4, verbose_name="میزان زمین (هکتار)")
    withdrawal_amount = models.DecimalField(max_digits=12, decimal_places=4, verbose_name="مقدار برداشت پیش‌بینی شده")
    date_set = models.DateTimeField(null=True, blank=True, verbose_name="تاریخ ثبت تعهد")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "تعهد کشاورز"
        verbose_name_plural = "تعهدات کشاورزان"