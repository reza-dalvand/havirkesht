from django.db import models
from common.models import MeasureUnit, Factory, CropYear
from farmer.models import Commitment, Farmer

class Seed(models.Model):
    id = models.BigAutoField(primary_key=True)
    seed_name = models.CharField(max_length=255, verbose_name="نام بذر")
    measure_unit = models.ForeignKey(MeasureUnit, on_delete=models.SET_NULL, null=True, related_name='seeds', verbose_name="واحد اندازه‌گیری")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "بذر"
        verbose_name_plural = "انواع بذر"


class Pesticide(models.Model):
    id = models.BigAutoField(primary_key=True)
    pesticide_name = models.CharField(max_length=255, verbose_name="نام سم")
    measure_unit = models.ForeignKey(MeasureUnit, on_delete=models.SET_NULL, null=True, related_name='pesticides', verbose_name="واحد اندازه‌گیری")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "سموم"
        verbose_name_plural = "انواع سموم"


class FactorySeed(models.Model):
    id = models.BigAutoField(primary_key=True)
    factory = models.ForeignKey(Factory, on_delete=models.CASCADE, related_name='factory_seeds', verbose_name="کارخانه")
    seed = models.ForeignKey(Seed, on_delete=models.CASCADE, related_name='factory_seeds', verbose_name="بذر")
    crop_year = models.ForeignKey(CropYear, on_delete=models.CASCADE, related_name='factory_seeds', verbose_name="سال زراعی")
    amount = models.DecimalField(max_digits=12, decimal_places=4, verbose_name="مقدار موجودی")
    farmer_price = models.DecimalField(max_digits=12, decimal_places=4, verbose_name="قیمت برای کشاورز")
    factory_price = models.DecimalField(max_digits=12, decimal_places=4, verbose_name="قیمت برای کارخانه")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "بذر کارخانه"
        verbose_name_plural = "بذرهای کارخانه"


class FactoryPesticide(models.Model):
    id = models.BigAutoField(primary_key=True)
    factory = models.ForeignKey(
        Factory,
        on_delete=models.CASCADE,
        related_name='factory_pesticides',
        verbose_name="کارخانه"
    )
    pesticide = models.ForeignKey(
        Pesticide,
        on_delete=models.CASCADE,
        related_name='factory_pesticides',
        verbose_name="سم"
    )
    crop_year = models.ForeignKey(
        CropYear,
        on_delete=models.CASCADE,
        related_name='factory_pesticides',
        verbose_name="سال زراعی"
    )
    amount = models.DecimalField(max_digits=12, decimal_places=4, verbose_name="مقدار موجودی")
    farmer_price = models.DecimalField(max_digits=12, decimal_places=4, verbose_name="قیمت برای کشاورز")
    factory_price = models.DecimalField(max_digits=12, decimal_places=4, verbose_name="قیمت برای کارخانه")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "سموم کارخانه"
        verbose_name_plural = "سموم کارخانه"


class FarmersSeed(models.Model):
    id = models.BigAutoField(primary_key=True)
    commitment = models.ForeignKey(Commitment, on_delete=models.CASCADE, related_name='seeds_distributed', verbose_name="تعهد")
    seed = models.ForeignKey(Seed, on_delete=models.CASCADE, related_name='farmers_seeds', verbose_name="بذر توزیع شده")
    factory = models.ForeignKey(Factory, on_delete=models.CASCADE, related_name='farmers_seeds', verbose_name="کارخانه توزیع کننده")
    crop_year = models.ForeignKey(CropYear, on_delete=models.CASCADE, related_name='farmers_seeds', verbose_name="سال زراعی")
    seed_amount = models.DecimalField(max_digits=12, decimal_places=4, verbose_name="مقدار بذر")
    price = models.DecimalField(max_digits=12, decimal_places=4, verbose_name="قیمت کل")
    price_for_all_farmers_check = models.BooleanField(default=False, verbose_name="بررسی قیمت برای همه کشاورزان")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "بذر توزیع شده به کشاورز"
        verbose_name_plural = "بذرهای توزیع شده"


class FarmersPesticide(models.Model):
    id = models.BigAutoField(primary_key=True)
    commitment = models.ForeignKey(Commitment, on_delete=models.CASCADE, related_name='pesticides_distributed', verbose_name="تعهد")
    pesticide = models.ForeignKey(Pesticide, on_delete=models.CASCADE, related_name='farmers_pesticides',
                                  verbose_name="سم توزیع شده")
    factory = models.ForeignKey(Factory, on_delete=models.CASCADE, related_name='farmers_pesticides', verbose_name="کارخانه توزیع کننده")
    crop_year = models.ForeignKey(CropYear, on_delete=models.CASCADE, related_name='farmers_pesticides', verbose_name="سال زراعی")
    pesticide_amount = models.DecimalField(max_digits=12, decimal_places=4, verbose_name="مقدار سم")
    price = models.DecimalField(max_digits=12, decimal_places=4, verbose_name="قیمت کل")
    price_for_all_farmers_check = models.BooleanField(default=False, verbose_name="بررسی قیمت برای همه کشاورزان")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "سم توزیع شده به کشاورز"
        verbose_name_plural = "سموم توزیع شده"


class FactorySugar(models.Model):
    id = models.BigAutoField(primary_key=True)
    factory = models.ForeignKey(
        Factory,
        on_delete=models.CASCADE,
        related_name='factory_sugar',
        verbose_name="کارخانه"
    )

    crop_year = models.ForeignKey(
        CropYear,
        on_delete=models.CASCADE,
        related_name='factory_sugar',
        verbose_name="سال زراعی"
    )
    sugar_weight_received_factory = models.DecimalField(max_digits=12, decimal_places=4, verbose_name="وزن شکر دریافتی")
    sugar_price_received_factory = models.DecimalField(max_digits=12, decimal_places=4, verbose_name="قیمت شکر دریافتی")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "شکر کارخانه"
        verbose_name_plural = "شکر کارخانه"


class FactoryWaste(models.Model):
    id = models.BigAutoField(primary_key=True)
    factory = models.ForeignKey(
        Factory,
        on_delete=models.CASCADE,
        related_name='factory_waste',
        verbose_name="کارخانه"
    )

    crop_year = models.ForeignKey(
        CropYear,
        on_delete=models.CASCADE,
        related_name='factory_waste',
        verbose_name="سال زراعی"
    )
    waste_weight_received_factory = models.DecimalField(max_digits=12, decimal_places=4,
                                                        verbose_name="وزن ضایعات دریافتی")
    waste_price_received_factory = models.DecimalField(max_digits=12, decimal_places=4,
                                                       verbose_name="قیمت ضایعات دریافتی")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "ضایعات کارخانه"
        verbose_name_plural = "ضایعات کارخانه"


class FarmersSugarDelivery(models.Model):
    id = models.BigAutoField(primary_key=True)
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE, related_name='sugar_deliveries', verbose_name="کشاورز")
    crop_year = models.ForeignKey(CropYear, on_delete=models.CASCADE, related_name='sugar_deliveries', verbose_name="سال زراعی")
    sugar_delivered = models.DecimalField(max_digits=12, decimal_places=4, verbose_name="شکر تحویل داده شده")
    sugar_deposit_amount = models.DecimalField(max_digits=12, decimal_places=4, verbose_name="مقدار ودیعه شکر")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "تحویل شکر کشاورز"
        verbose_name_plural = "تحویل شکر کشاورزان"


class FarmersWasteDelivery(models.Model):
    id = models.BigAutoField(primary_key=True)
    farmer = models.ForeignKey(
        Farmer,
        on_delete=models.CASCADE,
        related_name='waste_deliveries',
        verbose_name="کشاورز"
    )
    crop_year = models.ForeignKey(
        CropYear,
        on_delete=models.CASCADE,
        related_name='farmers_waste_deliveries',
        verbose_name="سال زراعی"
    )
    waste_delivered = models.DecimalField(max_digits=12, decimal_places=4, verbose_name="ضایعات تحویل داده شده")
    waste_deposit_amount = models.DecimalField(max_digits=12, decimal_places=4, verbose_name="مقدار ودیعه ضایعات")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "تحویل ضایعات کشاورز"
        verbose_name_plural = "تحویل ضایعات کشاورزان"