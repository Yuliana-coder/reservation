from django.db import models


class Restaurant(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=1000)
    address = models.CharField(max_length=200)


    def __str__(self):
        return self.title


class Order(models.Model):
    clientName = models.CharField(max_length=150)
    orderDate = models.DateField(auto_now_add=True)
    orderTime = models.TimeField()
    numberTable = models.IntegerField(default=1)
    dishList = models.ManyToManyField('Dish', verbose_name='dishList', null=True)
    quantityArray = models.CharField(max_length=700, null=True)


    def __str__(self):
        return self.clientName


class Table(models.Model):
    number = models.IntegerField(default=1)
    quantityPlaces = models.IntegerField(default=1)


class Dish(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=400)
    weight = models.IntegerField(default=50)
    price = models.IntegerField(default=50)




class Comment(models.Model):
    clientName = models.CharField(max_length=150)
    content = models.CharField(max_length=400)
    dish = models.ForeignKey('Dish', on_delete=models.DO_NOTHING, default=1)


class JobVacancy(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=800)
    salary = models.IntegerField(default=20000)
    duties = models.CharField(max_length=400)
    demands = models.CharField(max_length=400)


class JobApplication(models.Model):
    name = models.CharField(max_length=150)
    surname = models.CharField(max_length=150)
    patronymic = models.CharField(max_length=150)
    email = models.EmailField(max_length=254, null=True)
    phonenumber = models.CharField(max_length=15)
    vacancy = models.ForeignKey('JobVacancy', on_delete=models.DO_NOTHING, default=1)
