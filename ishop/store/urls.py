from django.conf.urls import url
from store import views



#Template tagging

app_name = 'store'

urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name="user_login"),
    url(r'^products/(?P<id>[0-9]+)/$',views.products,name="products"),
    url(r'^shoppingcart/$', views.shoppingcart, name="shoppingcart"),
    url(r'^add_item_to_cart/$', views.add_item_to_cart, name="add_item_to_cart"),
    url(r'^update_shoppingcart/$', views.update_shoppingcart, name="update_shoppingcart"),
    url(r'^checkout/$', views.checkout, name="checkout"),
    url(r'^order/$', views.place_order, name="order"),
    url('productdetails/(?P<id>[0-9]+)/$',views.productdetails,name="productdetails"),
] 
