from django.contrib import admin
from store.models import Product,Category,Inventory,CartItem,OrderDetail,Order,Customer

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Inventory)
admin.site.register(CartItem)
admin.site.register(OrderDetail)
admin.site.register(Order)
admin.site.register(Customer)




