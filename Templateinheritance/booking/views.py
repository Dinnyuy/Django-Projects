from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookingForm
from .models import Booking  # <-- Make sure you import the model

def book_session(request):
    if request.method == 'POST':
        form = BookingForm(request.POST, request.FILES)
        if form.is_valid():
            booking = form.save()
            return redirect('booking_detail', booking_id=booking.id)  # 👈 Redirect to detail view
    else:
        form = BookingForm()
    return render(request, 'booking/booking.html', {'form': form})

def booking_detail(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id)  # Safer than .get()
    return render(request, 'booking/booking_detail.html', {'booking': booking})
