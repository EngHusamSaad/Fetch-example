from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)  # اسم المنتج
    price = models.DecimalField(max_digits=10, decimal_places=2)  # سعر المنتج
    description = models.TextField()  # وصف المنتج

    def __str__(self):
        return self.name