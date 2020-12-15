from .models import Restaurant, Order, Table, Dish, Comment, JobVacancy, JobApplication
from rest_framework import viewsets,permissions
from .serializers import RestaurantSerializer, OrderSerializer, TableSerializer, DishSerializer,\
 CommentSerializer, JobVacancySerializer, JobApplicationSerializer


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = RestaurantSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = OrderSerializer


class TableViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TableSerializer


class DishViewSet(viewsets.ModelViewSet):
    queryset = Dish.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = DishSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CommentSerializer


class JobVacancyViewSet(viewsets.ModelViewSet):
    queryset = JobVacancy.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = JobVacancySerializer


class JobApplicationViewSet(viewsets.ModelViewSet):
    queryset = JobApplication.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = JobApplicationSerializer
