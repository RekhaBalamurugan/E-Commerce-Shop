from django.conf.urls import url
from store import views



#Template tagging

app_name = 'store'

urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name="user_login"),
    url(r'^products/$',views.products,name="products"),
    url(r'^shoppingcart/$', views.shoppingcart, name="shoppingcart"),
    url('productdetails/(?P<id>[0-9]+)/$',views.productdetails,name="productdetails"),
] 
