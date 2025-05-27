from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        "course": "Python Django",
        "City" : "Yaounde"
    }
    return render(request, 'base.html', context)

def home2(request):
    return render(request, 'user/index.html')