from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def blog_view(request):
    return HttpResponse("This is the blog section of our page where we post skincare content")