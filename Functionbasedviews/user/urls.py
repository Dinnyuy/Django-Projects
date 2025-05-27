from django.urls import path
from . import views

urlpatterns = [
    path("",views.home, name = "myhome", kwargs={"Name":"CEO Betty"}),
    path("about/", views.about, name="myabout"),
    path("contact/", views.contact, name="mycontact")
]
