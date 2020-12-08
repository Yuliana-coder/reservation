from rest_framework import routers
from .api import RestaurantViewSet, OrderViewSet, TableViewSet


router = routers.DefaultRouter()
router.register('api/restaurant', RestaurantViewSet, 'restaurant')
router.register('api/order', OrderViewSet, 'order')
router.register('api/table', TableViewSet, 'table')


urlpatterns = router.urls

