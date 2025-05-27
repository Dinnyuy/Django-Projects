from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def store_view(request):
    return HttpResponse("Welcome to the store where you can select the products you want")
