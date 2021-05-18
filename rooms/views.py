from django.shortcuts import render, get_object_or_404, redirect
from accounts.forms import User
from .models import RoomModel, BookingRoomModel
from .forms import RoomBookForm


def rooms_list(request):
    context = RoomModel.objects
    return render(request, 'rooms/rooms_list.html', {'context': context})


def rooms_booking(request, room_id):
    context = get_object_or_404(RoomModel, pk=room_id)
    already_book = BookingRoomModel.objects.filter(room_name_id=room_id).order_by('start')
    price = RoomModel.objects.get(pk=room_id).price
    if request.method == 'POST':
        form = RoomBookForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            for item in already_book:
                if new_form.start < item.end and new_form.end > item.start:
                    return render(request, 'rooms/error_message.html', )
            new_form.name = User.objects.get(username=request.user.username)
            new_form.room_name = RoomModel.objects.get(pk=room_id)
            new_form.save()
            return redirect(f'/hotel/rooms/booking/pay/{room_id}/{new_form.id}')
    else:
        form = RoomBookForm()
    return render(request, 'rooms/rooms_booking.html', {
        'context': context,
        'room': form,
        'book': already_book,
        'price': price,
    })


def hotel_view(request):
    return render(request, 'rooms/hotel.html')


def rooms_show(request):
    tmp = BookingRoomModel.objects.all().order_by('start')
    book_lst = []
    for obj in tmp:
        if str(obj.name) == request.user.username:
            book_lst.append([obj, get_object_or_404(RoomModel, name=str(obj.room_name))])
    return render(request, 'rooms/rooms_show.html', {'list': book_lst})


def rooms_pay(request, room_id, booking_id):
    context = get_object_or_404(RoomModel, pk=room_id)
    booking_room = BookingRoomModel.objects.get(pk=booking_id)
    end = int(booking_room.end.__format__('%d'))
    start = int(booking_room.start.__format__('%d'))
    price = RoomModel.objects.get(pk=room_id).price * (end - start)
    if request.method == 'POST':
        booking_room.price = price
        booking_room.save()
        return render(request, 'rooms/success.html', {'context': context, })
    return render(request, 'rooms/pay.html', {'context': context, 'price': price, })


def rooms_success(request, room_id):
    context = get_object_or_404(RoomModel, pk=room_id)
    return render(request, 'rooms/success.html', {'context': context, })
