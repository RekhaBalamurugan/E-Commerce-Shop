""" from django.db import models

# Create your models here.
class ProductDetails(models.Model):
    name= models.CharField(max_length=255)
    price= models.IntegerField()
    description=models.CharField(max_length=500)
    category_id=models.IntegerField()
    inventory_id=models.IntegerField()
    image=models.ImageField(default='cart.png',blank=True)    

    def __str__(self):
        return self.name
 """

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfileInfo(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    first_name = models.Field(blank=True)
    last_name = models.Field(blank=True)

    def __str__(self):
        return self.user.username


class Cart(models.Model):
    session_id = models.CharField(max_length=100)

    class Meta:
        managed = True


class Category(models.Model):
    ref = models.ForeignKey("self", models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=100)

    class Meta:
        managed = True


class Inventory(models.Model):
    quantity = models.IntegerField()

    class Meta:
        managed = True


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.CharField(max_length=100, blank=True, null=True)
    image1_url = models.CharField(max_length=255, blank=True, null=True)
    image2_url = models.CharField(max_length=255, blank=True, null=True)
    image3_url = models.CharField(max_length=255, blank=True, null=True)
    image4_url = models.CharField(max_length=255, blank=True, null=True)
    category = models.ForeignKey(Category, models.DO_NOTHING)
    inventory = models.ForeignKey(Inventory, models.DO_NOTHING)

    class Meta:
        managed = True


class CartItem(models.Model):
    quantity = models.IntegerField()
    product = models.ForeignKey(Product, models.DO_NOTHING)
    cart = models.ForeignKey(Cart, models.DO_NOTHING)

    class Meta:
        managed = True


class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    cart = models.ForeignKey(Cart, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True


class ShippingAddress(models.Model):
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zipcode = models.IntegerField()
    country = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True


class Payment(models.Model):
    amount = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = True


class Order(models.Model):
    amount = models.IntegerField()
    shipping_address = models.ForeignKey(ShippingAddress, models.DO_NOTHING)
    customer = models.ForeignKey(Customer, models.DO_NOTHING)
    payment = models.ForeignKey(Payment, models.DO_NOTHING)

    class Meta:
        managed = True


class OrderDetail(models.Model):
    quantity = models.IntegerField()
    product = models.ForeignKey(Product, models.DO_NOTHING)
    order = models.ForeignKey(Order, models.DO_NOTHING)

    class Meta:
        managed = True
