from django.shortcuts import render

# Create your views here.
def index(request):
    #var = 10
    #context = {"var":var}
    context = {
        #"is_logged_user" : True
       "user" : {"FullName": "Bongmoyong Betty", "Email":"bettorgaincsandspa@gmail.com", "Phone":+237677067324, "Membership":"Platinum",},
       "text" : "Hello world",
       "items" : ["apple", "banana", "cherry"],
       "price" : 56000,
       "date" : "2025-05-26",
       "html_content" : "<strong>Bold Text</strong>"
    }
       
    
    return render(request, 'user/index.html', context)