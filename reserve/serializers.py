from rest_framework import serializers
from .models import Restaurant, Order, Table, Dish, Comment, JobVacancy, JobApplication, New, Responsible,\
    PetitionReason, Appeal


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class JobVacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = JobVacancy
        fields = '__all__'


class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = '__all__'


class NewSerializer(serializers.ModelSerializer):
    class Meta:
        model = New
        fields = '__all__'


class ResponsibleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Responsible
        fields = '__all__'


class PetitionReasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetitionReason
        fields = '__all__'


class AppealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appeal
        fields = '__all__'
