from rest_framework.routers import DefaultRouter
from .views import (
    ProvinceViewSet, CityViewSet, VillageViewSet,
    FarmerViewSet, SupervisorViewSet, CommitmentViewSet
)

router = DefaultRouter()
router.register("province", ProvinceViewSet)
router.register("city", CityViewSet)
router.register("village", VillageViewSet)
router.register("farmer", FarmerViewSet)
router.register("supervisor", SupervisorViewSet)
router.register("commitment", CommitmentViewSet)

urlpatterns = router.urls
