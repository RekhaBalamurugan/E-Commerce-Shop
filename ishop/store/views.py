from django.shortcuts import render
#from store.models import ProductDetails
from django.views.generic import DetailView
from view_breadcrumbs import DetailBreadcrumbMixin

# Create your views here.


def index(request):
    return render(request, 'store/index.html')


def user_login(request):
    return render(request, 'store/login.html')

# Rekha


def products(request):
    products = ProductDetails.objects.all()
    my_dic = {'products': products}
    return render(request, "store/product.html", context=my_dic)


def cart(request):
    return render(request, "store/cart.html")

'''
def productdetails(request, id):
    itemdetail = ProductDetails.objects.filter(id=id).first
    dict = {'itemdetail': itemdetail}
    return render(request, "store/productdetails.html", context=dict)
'''