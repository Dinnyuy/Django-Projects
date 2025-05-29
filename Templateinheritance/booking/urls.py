from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_session, name='book_session'),
    path('booking/<int:booking_id>/', views.booking_detail, name='booking_detail'),  # 👈 This one
]
