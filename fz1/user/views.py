from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("<h1>Welcome to Bett's Organics and Spa</h1>")