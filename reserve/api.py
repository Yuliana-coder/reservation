from .models import Restaurant, Order, Table
from rest_framework import viewsets,permissions
from .serializers import RestaurantSerializer, OrderSerializer, TableSerializer


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

