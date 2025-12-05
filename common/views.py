from rest_framework import viewsets, status, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from django.contrib.auth import authenticate

from .models import Users, CropYear, Factory, MeasureUnit, PaymentReason
from .serializers import *
from .pagination import CustomPagination


class LoginView(APIView):
    """"""
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)

            if user:
                #todo: implement jwt token logic hear
                return Response({
                    "access_token": "fake-jwt-access-token",
                    "refresh_token": "fake-jwt-refresh-token",
                    "token_type": "bearer"
                })
            return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class RefreshTokenView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        refresh_token = request.query_params.get('refresh_token')
        if refresh_token:
            # todo: implement refresh token logic hear
            return Response({
                "access_token": "new-fake-access-token",
                "refresh_token": "new-fake-refresh-token",
                "token_type": "bearer"
            })
        return Response({"detail": "Missing refresh token"}, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # todo: send token to black list
        return Response({"message": "Successfully logged out"})


class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

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