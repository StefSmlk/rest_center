from django.contrib import admin

from rooms.models import RoomModel, BookingRoomModel

admin.site.register(RoomModel)
admin.site.register(BookingRoomModel)
