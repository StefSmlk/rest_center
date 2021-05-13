from django.shortcuts import render, get_object_or_404, redirect

from accounts.forms import User
from .models import RoomModel
from .forms import RoomBookForm


def rooms_list(request):
    context = RoomModel.objects
    return render(request, 'rooms/rooms_list.html', {'context': context})


def rooms_booking(request, room_id):
    context = get_object_or_404(RoomModel, pk=room_id)
    if request.method == 'POST':
        form = RoomBookForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.name = User.objects.get(username=request.user.username)
            new_form.save()
    else:
        form = RoomBookForm()
    return render(request, 'rooms/rooms_booking.html', {'context': context, 'room': form})


def hotel_view(request):
    return render(request, 'rooms/hotel.html')
