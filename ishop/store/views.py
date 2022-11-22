from django.shortcuts import render
from store.models import Product, CartItem, Category
from store.forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from store.models import *
from django.template.defaultfilters import register

@register.filter(name='dict_key')
def dict_key(dict, key):
    return dict[key]

def getCategoryList():
    categorylist = {}
    for category in Category.objects.filter(ref__isnull=True):
        categorylist[category.name] = Category.objects.filter(ref__id=category.id)
    return categorylist

def get_or_create_session_key(request):
    if not request.session.session_key:
        request.session.save()
    return request.session.session_key


def getCart(request):
    cart = Cart()
    if request.session.session_key:
        cart = Cart.get_or_create_cart(request.session.session_key)
    return cart

# Create your views here.


def index(request):
    cart = getCart(request)

    

    return render(request, 'store/index.html',  {'item_count': cart.get_total_qty(), 'total_amount': cart.get_total_amount(), 'categorylist': getCategoryList()})


def shoppingcart(request):

    cart = getCart(request)
    if cart.get_total_amount() <= 3000:
        shippingcost= cart.get_total_amount() + 69
    else:
        shippingcost = cart.get_total_amount()
    return render(request, 'store/shoppingcart.html', {'cart_items': cart.get_items(), 'item_count': cart.get_total_qty(), 'total_amount': cart.get_total_amount(), 'categorylist': getCategoryList(),'shippingcost':shippingcost})


def add_item_to_cart(request):

    get_or_create_session_key(request)
    cart = getCart(request)

    if request.method == 'POST' and 'request_path' in request.POST:
        item_id = int(request.POST.get('item_id'))
        qty = int(request.POST.get('add_btn'))

        cart.add_item(item_id, qty)

        return HttpResponseRedirect(request.POST.get('request_path'))

    return HttpResponseRedirect(reverse('index'))


def update_shoppingcart(request):

    cart = getCart(request)

    if request.method == "POST":

        item_id = int(request.POST.get('item_id'))
        qty = int(request.POST.get('item_qty'))

        cart.update_item(item_id, qty)
    return HttpResponseRedirect(request.POST.get('request_path'))


def checkout(request):
    cart = getCart(request)
    return render(request, 'store/checkout.html', {'item_count': cart.get_total_qty(), 'total_amount': cart.get_total_amount(), 'categorylist': getCategoryList()})


@login_required
def special(request):
    return HttpResponse("you are logged in!,Nice!")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):

    cart = getCart(request)
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()

    return render(request, 'store/registration.html',
                  {'user_form': user_form,
                   'registered': registered,
                   'cart_items': cart.get_items(),
                   'item_count': cart.get_total_qty(),
                   'total_amount': cart.get_total_amount()})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        print(user)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('Account not active')
        else:
            print("someone tried to log in and failed!")
            print("username: {} and password {}".format(username, password))
            return HttpResponse('invalid login details')
    else:
        return render(request, 'store/login.html', {})


def products(request, id):
    cart = getCart(request)
    products = Product.objects.filter(category_id=id)
    my_dic = {'products': products, 'item_count': cart.get_total_qty(
    ), 'total_amount': cart.get_total_amount(), 'categorylist': getCategoryList()}
    return render(request, "store/product.html", context=my_dic)


def productdetails(request, id):

    cart = getCart(request)
    itemdetail = Product.objects.filter(id=id).first
    dict = {'itemdetail': itemdetail, 'item_count': cart.get_total_qty(
    ), 'total_amount': cart.get_total_amount(), 'categorylist': getCategoryList()}
    return render(request, "store/productdetails.html", context=dict)


def search(request):
    cart = getCart(request)
    if request.method == 'GET':
        searchresult = request.GET.get('searchtext')
        return_url = "?searchtext={0}".format(searchresult)
        if searchresult:
            products = Product.objects.filter(name__icontains=searchresult)
            return render(request, 'store/searchpage.html', {'return_url': return_url, 'products': products, 'item_count': cart.get_total_qty(), 'total_amount': cart.get_total_amount(), 'categorylist': getCategoryList()})
        else:
            print("No matching item found")
            return render(request, 'store/searchpage.html', {'item_count': cart.get_total_qty(), 'total_amount': cart.get_total_amount(), 'categorylist': getCategoryList()})
