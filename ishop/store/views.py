from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'store/index.html')

def user_login(request):
    return render(request, 'store/login.html')