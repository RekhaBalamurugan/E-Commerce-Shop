from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from store.forms import UserForm,UserProfileInfo

# Create your views here.

def index(request):
    return render(request, 'store/index.html')

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
