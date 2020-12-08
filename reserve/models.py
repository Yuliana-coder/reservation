from django.db import models


class Restaurant(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=550)
    address = models.CharField(max_length=200)


    def __str__(self):
        return self.title


class Order(models.Model):
    clientName = models.CharField(max_length=150)
    orderDate = models.DateField(auto_now_add=True)
    orderTime = models.TimeField()
    numberTable = models.IntegerField(default=1)


    def __str__(self):
        return self.clientName


class Table(models.Model):
    number = models.IntegerField(default=1)
    quantityPlaces = models.IntegerField(default=1)

    # def __str__(self):
    #     return self.quantityPlaces

