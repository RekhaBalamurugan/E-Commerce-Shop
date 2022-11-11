from django.conf.urls import url
from store import views



#Template taging

app_name = 'store'

urlpatterns = [
    url(r'^login/$', views.user_login, name="user_login"),
] 