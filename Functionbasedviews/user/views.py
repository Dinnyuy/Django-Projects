from django.shortcuts import render
from django.http import HttpResponse
def home(request, Name = None):
    print("This is the value from pathfunction",Name)
    #var=request.GET.get("name")
    #print(var)
    context = {"Name":"CEO Betty", "ID":"5637365"}
    return render(request, 'index.html', context)
def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")