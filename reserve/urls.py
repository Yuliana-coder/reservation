from rest_framework import routers
from .api import RestaurantViewSet, OrderViewSet, TableViewSet, DishViewSet, CommentViewSet, JobVacancyViewSet, JobApplicationViewSet


router = routers.DefaultRouter()
router.register('api/restaurant', RestaurantViewSet, 'restaurant')
router.register('api/order', OrderViewSet, 'order')
router.register('api/table', TableViewSet, 'table')
router.register('api/dish', DishViewSet, 'dish')
router.register('api/comment', CommentViewSet, 'comment')
router.register('api/jobvacancy', JobVacancyViewSet, 'jobvacancy')
router.register('api/jobapplication', JobApplicationViewSet, 'jobapplication')

urlpatterns = router.urls

