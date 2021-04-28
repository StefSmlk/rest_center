from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import RoomModel
from .forms import RoomBookForm


def rooms_list(request):
    context = RoomModel.objects
    return render(request, 'rooms/rooms_list.html', {'context': context})


def rooms_booking(request, room_id):
    context = get_object_or_404(RoomModel, pk=room_id)
    room = RoomBookForm(request.POST or None)
    return render(request, 'rooms/rooms_booking.html', {'context': context, 'room': room})


def hotel_view(request):
    return render(request, 'rooms/hotel.html')
