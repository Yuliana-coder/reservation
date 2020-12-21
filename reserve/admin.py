from django.contrib import admin
from .models import Restaurant, Order, Table, Dish, Comment, JobVacancy, JobApplication, New


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


class JobVacancyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'salary','duties', 'demands')
    list_display_links = ('id', 'name', 'description', 'salary','duties', 'demands')
    search_fields = ('id', 'name', 'description')


admin.site.register(JobVacancy, JobVacancyAdmin)


class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'patronymic','email', 'phonenumber', 'vacancy')
    list_display_links = ('id', 'name', 'surname', 'patronymic','email', 'phonenumber', 'vacancy')
    search_fields = ('id', 'name', 'surname', 'patronymic')


admin.site.register(JobApplication, JobApplicationAdmin)


class NewAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'articleTopic', 'description','datePublication')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title', 'description')


admin.site.register(New, NewAdmin)
