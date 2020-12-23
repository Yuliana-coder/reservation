from rest_framework import routers
from .api import RestaurantViewSet, OrderViewSet, TableViewSet, DishViewSet, CommentViewSet, JobVacancyViewSet, \
    JobApplicationViewSet, NewViewSet, ResponsibleViewSet, PetitionReasonViewSet, AppealViewSet


router = routers.DefaultRouter()
router.register('api/restaurant', RestaurantViewSet, 'restaurant')
router.register('api/order', OrderViewSet, 'order')
router.register('api/table', TableViewSet, 'table')
router.register('api/dish', DishViewSet, 'dish')
router.register('api/comment', CommentViewSet, 'comment')
router.register('api/jobvacancy', JobVacancyViewSet, 'jobvacancy')
router.register('api/jobapplication', JobApplicationViewSet, 'jobapplication')
router.register('api/new', NewViewSet, 'new')
router.register('api/responsible', ResponsibleViewSet, 'responsible')
router.register('api/petitionreason', PetitionReasonViewSet, 'petitionreason')
router.register('api/appeal', AppealViewSet, 'appeal')

urlpatterns = router.urls

