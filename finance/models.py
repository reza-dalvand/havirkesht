from django.db import models
from common.models import CropYear, PaymentReason, Users, Factory
from farmer.models import Farmer


class PurityPrice(models.Model):
    id = models.BigAutoField(primary_key=True)
    crop_year = models.ForeignKey(
        CropYear,
        on_delete=models.CASCADE,
        related_name='purity_prices',
        verbose_name="سال زراعی"
    )
    base_purity = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name="خلوص پایه (درصد)"
    )
    base_purity_price = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        verbose_name="قیمت خلوص پایه"
    )
    price_difference = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        verbose_name="اختلاف قیمت خلوص"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "قیمت خلوص"
        verbose_name_plural = "قیمت‌های خلوص"

    def __str__(self):
        return f"قیمت خلوص پایه {self.base_purity}% در سال {self.crop_year_id}"

class ProductPrice(models.Model):
    id = models.BigAutoField(primary_key=True)

    crop_year = models.ForeignKey(
        'common.CropYear',
        on_delete=models.CASCADE,
        related_name='product_prices',
        verbose_name="سال زراعی"
    )
    sugar_amount_per_ton_kg = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        verbose_name="مقدار شکر به ازای تن (کیلوگرم)"
    )

    sugar_price_per_kg = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        verbose_name="قیمت شکر به ازای کیلوگرم"
    )

    # pulp_amount_per_ton_kg double precision
    pulp_amount_per_ton_kg = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        verbose_name="مقدار تفاله به ازای تن (کیلوگرم)"
    )
    pulp_price_per_kg = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        verbose_name="قیمت تفاله به ازای کیلوگرم"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "قیمت محصول"
        verbose_name_plural = "قیمت‌های محصول"

    def __str__(self):
        return f"قیمت محصولات سال {self.crop_year_id}"


class FarmersPayment(models.Model):
    id = models.BigAutoField(primary_key=True)
    payment_type = models.ForeignKey(
        PaymentReason,
        on_delete=models.SET_NULL,
        null=True,
        related_name='farmers_payments',
        verbose_name="نوع پرداخت"
    )
    farmer = models.ForeignKey(
        Farmer,
        on_delete=models.CASCADE,
        related_name='farmers_payments',
        verbose_name="کشاورز"
    )
    price = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        verbose_name="مبلغ پرداخت"
    )
    crop_year = models.ForeignKey(
        CropYear,
        on_delete=models.CASCADE,
        related_name='farmers_payments',
        verbose_name="سال زراعی"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "پرداخت کشاورز"
        verbose_name_plural = "پرداخت‌های کشاورزان"
        db_table = 'farmers_payment'

    def __str__(self):
        return f"پرداخت به {self.farmer_id} در سال {self.crop_year_id}"


class FarmersInvoicePayed(models.Model):
    id = models.BigAutoField(primary_key=True)

    farmer = models.ForeignKey(
        Farmer,
        on_delete=models.CASCADE,
        related_name='paid_invoices',
        verbose_name="کشاورز"
    )
    crop_year = models.ForeignKey(
        CropYear,
        on_delete=models.CASCADE,
        related_name='paid_invoices',
        verbose_name="سال زراعی"
    )
    payed = models.BooleanField(default=False, verbose_name="پرداخت شده")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "فاکتور پرداخت‌شده کشاورز"
        verbose_name_plural = "فاکتورهای پرداخت‌شده کشاورزان"
        db_table = 'farmers_invoice_payed'
        unique_together = ('farmer', 'crop_year')

    def __str__(self):
        status = "پرداخت شده" if self.payed else "در انتظار پرداخت"
        return f"فاکتور {status} کشاورز {self.farmer_id} در سال {self.crop_year_id}"


class FarmersGuarantee(models.Model):
    id = models.BigAutoField(primary_key=True)
    guarantor_farmer = models.ForeignKey(
        Farmer,
        on_delete=models.CASCADE,
        related_name='guarantees_given',
        verbose_name="کشاورز ضامن"
    )

    guaranteed_farmer = models.ForeignKey(
        'farmer.Farmer',
        on_delete=models.CASCADE,
        related_name='guarantees_received',
        verbose_name="کشاورز ضمانت‌شده"
    )

    guarantee_price = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        verbose_name="مبلغ ضمانت"
    )

    crop_year = models.ForeignKey(
        CropYear,
        on_delete=models.CASCADE,
        related_name='farmers_guarantees',
        verbose_name="سال زراعی"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "ضمانت کشاورز"
        verbose_name_plural = "ضمانت‌های کشاورزان"
        db_table = 'farmers_guarantee'

    def __str__(self):
        return f"ضمانت {self.guarantor_farmer_id} برای {self.guaranteed_farmer_id} در سال {self.crop_year_id}"


class FactoryPayment(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(
        Users,
        on_delete=models.SET_NULL,
        null=True,
        related_name='factory_payments',
        verbose_name="کاربر مسئول پرداخت"
    )
    crop_year = models.ForeignKey(
        CropYear,
        on_delete=models.CASCADE,
        related_name='factory_payments',
        verbose_name="سال زراعی"
    )

    factory = models.ForeignKey(
        Factory,
        on_delete=models.CASCADE,
        related_name='factory_payments',
        verbose_name="کارخانه"
    )
    title = models.CharField(max_length=255, verbose_name="عنوان پرداخت")
    date = models.DateTimeField(verbose_name="تاریخ پرداخت")
    price = models.DecimalField(max_digits=12, decimal_places=4, verbose_name="مبلغ")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "پرداخت کارخانه"
        verbose_name_plural = "پرداخت‌های کارخانه"
        db_table = 'factory_payment'

    def __str__(self):
        return f"پرداخت {self.title} کارخانه {self.factory_id} در سال {self.crop_year_id}"