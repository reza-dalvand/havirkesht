from tokenize import TokenError
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .serializers import *
from .pagination import CustomPagination


class LoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    # @swagger_auto_schema(
    #     # معرفی Serializer ورودی به متد POST
    #     request_body=CustomTokenObtainPairSerializer,
    #     # معرفی Serializer خروجی
    #     responses={200: TokenSerializer}
    # )
    # def post(self, request, *args, **kwargs):
    #     return super().post(request, *args, **kwargs)
class RefreshTokenView(TokenRefreshView):
    pass


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = LogoutSerializer

    def post(self, request):
        try:
            refresh_token = request.data.get("refresh_token")
            if not refresh_token:
                return Response({"detail": "Refresh token is required"}, status=status.HTTP_400_BAD_REQUEST)

            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response({"message": "Successfully logged out"}, status=status.HTTP_200_OK)
        except TokenError:
            return Response({"detail": "Invalid refresh token"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ChangePasswordSerializer
    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            if not user.check_password(serializer.validated_data['old_password']):
                return Response({"detail": "Wrong old password"}, status=status.HTTP_400_BAD_REQUEST)

            user.set_password(serializer.validated_data['new_password'])
            user.save()
            return Response({"message": "Password changed successfully"})
        return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ['update', 'partial_update']:
            return UserUpdateSerializer
        return UserOutSerializer

    @action(detail=False, methods=['post'], url_path='admin', serializer_class=UserCreateSerializer)
    def admin_create(self, request):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class UsersDashboardView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UsersDashboardResponseSerializer
    def get(self, request):
        user_id = request.query_params.get('user_id')
        crop_year_id = request.query_params.get('crop_year_id')

        data = {
            "farmer_id": int(user_id) if user_id else 0,
            "crop_year_id": int(crop_year_id) if crop_year_id else 0,
            "farmer_name": "Sample Farmer",
            "crop_year_name": "1403",
            "your_farming_profit": 100000,
            "total_seed_cost": 5000,
            "total_pesticide_cost": 2000,
            "total_paid_to_you": 50000,
            "total_delivered_load": 10,
            "total_weight_delivered": 1000,
            "total_pure_payable": 90000,
            "one_percent_deduction": 900,
            "remaining_to_settle": 40000,
            "sugar_quota": 50,
            "waste_quota": 200,
            "dashboard_generated_at": "2024-01-01 12:00:00"
        }
        serializer = UsersDashboardResponseSerializer(data=data)
        return Response(serializer.data)


class CropYearViewSet(viewsets.ModelViewSet):
    queryset = CropYear.objects.all()
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return CropYearCreateSerializer
        return CropYearResponseSerializer


class FactoryViewSet(viewsets.ModelViewSet):
    queryset = Factory.objects.all()
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return FactoryCreateSerializer
        return FactoryResponseSerializer


class MeasureUnitViewSet(viewsets.ModelViewSet):
    queryset = MeasureUnit.objects.all()
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return MeasureUnitCreateSerializer
        return MeasureUnitResponseSerializer


class PaymentReasonViewSet(viewsets.ModelViewSet):
    queryset = PaymentReason.objects.all()
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return PaymentReasonCreateSerializer
        return PaymentReasonResponseSerializer