from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, PurchaseViewSet, ReservationViewSet, TheaterViewSet, ShowtimeViewSet

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'theaters', TheaterViewSet)
router.register(r'showtimes', ShowtimeViewSet)
router.register(r'reservations', ReservationViewSet)
router.register(r'purchases', PurchaseViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
