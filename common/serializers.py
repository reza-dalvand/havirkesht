from rest_framework import serializers
from .models import Users, CropYear, Factory, MeasureUnit, PaymentReason, Roles


class TokenSerializer(serializers.Serializer):
    access_token = serializers.CharField()
    refresh_token = serializers.CharField()
    token_type = serializers.CharField()


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    new_password_repeat = serializers.CharField(required=True)


class UserCreateSerializer(serializers.ModelSerializer):
    role_id = serializers.IntegerField()

    class Meta:
        model = Users
        fields = ('username', 'password', 'fullname', 'email', 'disabled', 'role_id', 'phone_number')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        role_id = validated_data.pop('role_id')
        role = Roles.objects.get(id=role_id)
        password = validated_data.pop('password')

        user = Users.objects.create_user(
            role_id=role,
            password=password,
            **validated_data
        )
        return user


class UserUpdateSerializer(serializers.ModelSerializer):
    role_id = serializers.IntegerField(required=False)

    class Meta:
        model = Users
        fields = ('username', 'password', 'fullname', 'email', 'phone_number', 'role_id', 'disabled')
        extra_kwargs = {
            'username': {'required': False},
            'password': {'required': False, 'write_only': True},
            'fullname': {'required': False},
        }


class UserOutSerializer(serializers.ModelSerializer):
    role_id = serializers.PrimaryKeyRelatedField(read_only=True)
    created_at_jalali = serializers.CharField(read_only=True, required=False, allow_null=True)
    updated_at_jalali = serializers.CharField(read_only=True, required=False, allow_null=True)

    class Meta:
        model = Users
        fields = ('id', 'username', 'email', 'fullname', 'phone_number', 'role_id', 'disabled',
                  'created_at', 'updated_at', 'created_at_jalali', 'updated_at_jalali')


class CropYearCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = CropYear
        fields = ('crop_year_name',)


class CropYearResponseSerializer(serializers.ModelSerializer):

    class Meta:
        model = CropYear
        fields = ('id', 'crop_year_name', 'created_at')


class FactoryCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Factory
        fields = ('factory_name',)


class FactoryResponseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Factory
        fields = ('id', 'factory_name', 'created_at')


class MeasureUnitCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = MeasureUnit
        fields = ('unit_name',)


class MeasureUnitResponseSerializer(serializers.ModelSerializer):

    class Meta:
        model = MeasureUnit
        fields = ('id', 'unit_name', 'created_at')


class PaymentReasonCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = PaymentReason
        fields = ('reason_name',)


class PaymentReasonResponseSerializer(serializers.ModelSerializer):

    class Meta:
        model = PaymentReason
        fields = ('id', 'reason_name', 'created_at')


class UsersDashboardResponseSerializer(serializers.Serializer):
    farmer_id = serializers.IntegerField()
    crop_year_id = serializers.IntegerField()
    farmer_name = serializers.CharField()
    crop_year_name = serializers.CharField()
    your_farming_profit = serializers.DecimalField(max_digits=20, decimal_places=4)
    total_seed_cost = serializers.DecimalField(max_digits=20, decimal_places=4)
    total_pesticide_cost = serializers.DecimalField(max_digits=20, decimal_places=4)
    total_paid_to_you = serializers.DecimalField(max_digits=20, decimal_places=4)
    total_delivered_load = serializers.DecimalField(max_digits=20, decimal_places=4)
    total_weight_delivered = serializers.DecimalField(max_digits=20, decimal_places=4)
    total_pure_payable = serializers.DecimalField(max_digits=20, decimal_places=4)
    one_percent_deduction = serializers.DecimalField(max_digits=20, decimal_places=4)
    remaining_to_settle = serializers.DecimalField(max_digits=20, decimal_places=4)
    sugar_quota = serializers.DecimalField(max_digits=20, decimal_places=4)
    waste_quota = serializers.DecimalField(max_digits=20, decimal_places=4)
    dashboard_generated_at = serializers.CharField()