from django.db import models

from User.models import User
from Product.models import Product


class Cart(models.Model):
    customer_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    total = models.FloatField(default=0)

    def __str__(self):
        return str(self.user.username) + " " + str(self.total)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name='product')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    quantity = models.IntegerField(default=1)
    price = models.FloatField(default=0)
    discount = models.FloatField(default=0)


    def __str__(self):
        return str(self.user.username) + " " + str(self.user.product)