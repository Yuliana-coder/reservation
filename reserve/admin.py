from django.contrib import admin
from .models import Restaurant, Order, Table, Dish, Comment


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'address')


admin.site.register(Restaurant, RestaurantAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'clientName','orderDate', 'orderTime', 'numberTable')
    list_display_links = ('id', 'orderTime', 'clientName')
    search_fields = ('id', 'clientName', 'numberTable')


admin.site.register(Order, OrderAdmin)


class TableAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'quantityPlaces')
    list_display_links = ('id', 'quantityPlaces')


admin.site.register(Table, TableAdmin)


class DishAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description','weight', 'price')
    list_display_links = ('id', 'title', 'description','weight', 'price')
    search_fields = ('id', 'title', 'description')


admin.site.register(Dish, DishAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'clientName', 'content','dish')
    list_display_links = ('id', 'clientName', 'content','dish')
    search_fields = ('id', 'clientName', 'content')


admin.site.register(Comment, CommentAdmin)
