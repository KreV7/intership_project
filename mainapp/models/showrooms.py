from django.db import models
from django_countries.fields import CountryField

from .suppliers import Supplier, SuppliersGarage
from .customers import AdvUser


class Showroom(models.Model):
    title = models.CharField(max_length=256)
    location = CountryField()
    parameters_car = models.JSONField()
    cash_balance = models.DecimalField(max_digits=25, decimal_places=2)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updates = models.DateTimeField(auto_now=True)


class ShowroomsGarage(models.Model):
    car = models.ForeignKey(SuppliersGarage, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    purchase_price = models.DecimalField(max_digits=25, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    selling_price = models.DecimalField(max_digits=25, decimal_places=2)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updates = models.DateTimeField(auto_now=True)


class ShowroomCustomerHistory(models.Model):
    customer = models.ForeignKey(AdvUser, on_delete=models.CASCADE)
    car = models.ForeignKey(ShowroomsGarage, on_delete=models.CASCADE)
    showroom = models.ForeignKey(Showroom, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=25, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    total_cost = models.DecimalField(max_digits=25, decimal_places=2)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)


class SupplierSalesHistory(models.Model):
    showroom = models.ForeignKey(Showroom, on_delete=models.CASCADE)
    car = models.ForeignKey(SuppliersGarage, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=25, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=25, decimal_places=2)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
