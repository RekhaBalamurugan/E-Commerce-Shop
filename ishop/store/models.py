from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Cart(models.Model):
    session_id = models.CharField(max_length=100)

    class Meta:
        managed = True

    def get_or_create_cart(session_key):
        return Cart.objects.get_or_create(session_id=session_key)[0]

    def get_items(self):
        return CartItem.objects.filter(cart=self)

    def update_item(self, item_id, qty):

        item = CartItem.objects.filter(cart=self, product_id=item_id)

        if item.exists():
            item = item[0]
            if qty == 0:
                item.delete()
            else:
                item.quantity = qty
                item.save()


    def add_item(self, item_id, qty):

        item = CartItem.objects.filter(cart=self, product_id=item_id)

        if item.exists():
            item = item[0]
            item.quantity += qty
        else:
            item = CartItem()
            item.cart = self
            item.quantity = qty
            item.product = Product(id = item_id)

        item.save()

    def get_total_qty(self):
        item_count = 0
        for item in self.get_items():
            item_count += item.quantity
        return item_count

    def get_total_amount(self):
        total_amount = 0
        for item in self.get_items():
            total_amount += item.line_total()
        return total_amount

class Category(models.Model):
    ref = models.ForeignKey("self", models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=100)

    class Meta:
        managed = True
        
    def __str__(self):
        return self.name


class Inventory(models.Model):
    quantity = models.IntegerField()

    class Meta:
        managed = True


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.CharField(max_length=500, blank=True, null=True)
    image1_url = models.ImageField(default="placeholder.png", upload_to='images',blank=True)
    image2_url = models.ImageField(default="placeholder.png", upload_to='images',blank=True)
    image3_url = models.ImageField(default="placeholder.png", upload_to='images',blank=True)
    image4_url = models.ImageField(default="placeholder.png", upload_to='images',blank=True)
    category = models.ForeignKey(Category, models.DO_NOTHING)
    inventory = models.ForeignKey(Inventory, models.DO_NOTHING)

    def __str__(self):
        return self.name
    class Meta:
        managed = True


class CartItem(models.Model):
    quantity = models.IntegerField()
    product = models.ForeignKey(Product, models.DO_NOTHING)
    cart = models.ForeignKey(Cart, models.DO_NOTHING)

    class Meta:
        managed = True

    def line_total(self):
        return self.quantity * self.product.price

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
