from django.conf.urls import url
from store import views



#Template taging

app_name = 'store'

urlpatterns = [
    url(r'^login/$', views.user_login, name="user_login"),
    url(r'^products/$',views.products,name="products"),
    url(r'^cart/$',views.cart,name="cart"),
    #url('productdetails/(?P<id>[0-9]+)/$',views.productdetails,name="productdetails"),
] 