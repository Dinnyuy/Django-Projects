from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def cart_home(request):
    return HttpResponse("<h1> This is the cart page</h1>")