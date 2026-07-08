from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponseForbidden
from .models import Booking, Room


def home(request):
    return render(request, 'home.html')


def spaces(request):
    return render(request, 'spaces.html')


def details(request):
    return render(request, 'details.html')


def booking(request):
    return render(request, 'booking.html')


def confirmation(request):
    return render(request, 'confirmation.html')


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


@login_required
def reports(request):
    return render(request, 'reports.html')


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def edit_booking(request, booking_id):
    booking_item = get_object_or_404(Booking, id=booking_id)

    if not request.user.is_staff and not request.user.is_superuser:
        return redirect('home')

    rooms = Room.objects.all()

    if request.method == 'POST':
        room_id = request.POST.get('room')
        booking_date = request.POST.get('booking_date')
        hours = request.POST.get('hours')
        notes = request.POST.get('notes')

        booking_item.room = get_object_or_404(Room, id=room_id)
        booking_item.booking_date = booking_date
        booking_item.hours = hours
        booking_item.notes = notes
        booking_item.save()

        return redirect('dashboard')

    return render(request, 'edit_booking.html', {
        'booking': booking_item,
        'rooms': rooms,
    })


@login_required
def delete_booking(request, booking_id):
    if not request.user.is_superuser:
        return HttpResponseForbidden("Access denied")

    booking_item = get_object_or_404(Booking, id=booking_id)

    if request.method == 'POST':
        booking_item.delete()

    return redirect('dashboard')