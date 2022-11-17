from django.shortcuts import render
from store.models import Product
from store.forms import UserForm, UserProfileInfo
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from store.models import Cart


def get_or_create_session_key(request):
    if not request.session.session_key:
        request.session.save()
    return request.session.session_key

# Create your views here.

def index(request):

    cart = Cart()

    if request.session.session_key:
        cart = Cart.get_or_create_cart(request.session.session_key)

    return render(request, 'store/index.html', {'item_count':cart.get_items().count})

def shoppingcart(request):

    session_key = get_or_create_session_key(request)
    cart = Cart.get_or_create_cart(session_key)

    return render(request, 'store/shoppingcart.html', {'cart_items':cart.get_items(), 'item_count':cart.get_items().count})

@login_required
def special(request):
    return HttpResponse("you are logged in!,Nice!")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfo(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfo()

    return render(request, 'store/registration.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered})


def user_login(request):
    return render(request, 'store/login.html')

def register(request):
    registered= False

    if request.method =='POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfo(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            profile = profile_form.save(commit=False)
            profile.user = user
            registered = True
        else:
            print(user_form.errors,profile_form.errors)    

    else:
        user_form = UserForm()
        profile_form = UserProfileInfo()  

    return render(request,'store/registration.html',
                   {'user_form':user_form,
                   'profile_form':profile_form,
                   'registered':registered})  

def products(request):
    products = Product.objects.all()
    my_dic = {'products': products}
    return render(request, "store/product.html", context=my_dic)


def cart(request):
    return render(request, "store/cart.html")

def productdetails(request, id):
    itemdetail = Product.objects.filter(id=id).first
    dict = {'itemdetail': itemdetail}
    return render(request, "store/productdetails.html", context=dict)