from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'user/index.html')
def services(request):
    return render(request, 'user/coming_soon.html')

def shop(request):
    return render(request, 'user/coming_soon.html')
def about(request):
    return render(request, 'user/about.html')
def contact(request):
    return render(request, 'user/coming_soon.html')
