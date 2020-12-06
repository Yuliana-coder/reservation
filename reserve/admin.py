from django.contrib import admin
from .models import Restaurant


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'address')


admin.site.register(Restaurant, RestaurantAdmin)