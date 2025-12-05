from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class MeasureUnit(models.Model):
    id = models.BigAutoField(primary_key=True)
    unit_name = models.CharField(max_length=100, verbose_name="نام واحد")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CropYear(models.Model):
    id = models.BigAutoField(primary_key=True)
    crop_year_name = models.CharField(max_length=255, verbose_name="نام سال زراعی")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class PaymentReason(models.Model):
    id = models.BigAutoField(primary_key=True)
    reason_name = models.CharField(max_length=255, verbose_name="دلیل پرداخت")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class AlembicVersion(models.Model):
    version_num = models.CharField(
        max_length=32,
        primary_key=True,
        verbose_name="شماره نسخه Alembic"
    )

    class Meta:
        verbose_name = " Alembic"
        verbose_name_plural = "Alembic"

    def __str__(self):
        return self.version_num


class Factory(models.Model):
    id = models.BigAutoField(primary_key=True)
    factory_name = models.CharField(max_length=255, verbose_name="نام کارخانه")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    product_name = models.CharField(
        max_length=255,
        verbose_name="نام محصول",
        unique=True
    )
    measure_unit = models.ForeignKey(
        'MeasureUnit',
        on_delete=models.SET_NULL,
        null=True,
        related_name='products',
        verbose_name="واحد اندازه‌گیری"
    )
    crop_year = models.ForeignKey(
        'CropYear',
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name="سال زراعی"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"
        db_table = 'product'

    def __str__(self):
        return self.product_name

class Roles(models.Model):
    id = models.BigAutoField(primary_key=True)
    name_user_role = models.CharField(max_length=100, verbose_name="نقش کاربری")
    scopes = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, password, **extra_fields)


class Users(AbstractBaseUser):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    fullname = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    disabled = models.BooleanField(default=False)
    role_id = models.ForeignKey(Roles, on_delete=models.SET_NULL, null=True, related_name='users')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['fullname', 'email']

    objects = CustomUserManager()

    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربران"

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

    def __str__(self):
        return self.username

class TokenBlacklist(models.Model):
    token = models.CharField(max_length=255, verbose_name="توکن مسدود شده")
    blacklisted_at = models.DateTimeField(verbose_name="تاریخ مسدود شدن")
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "توکن مسدود شده"
        verbose_name_plural = "توکن‌های مسدود شده"

    def __str__(self):
        return f"Token: {self.token[:20]}..."