"""rest_center URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from rest_center.views import home
from rooms.views import rooms_list, rooms_booking, hotel_view, rooms_show, rooms_success, rooms_pay, booking_delete
from accounts.views import login_view, logout_view, sign_up_view
from forecasts.views import forecast_view
from ski_resort.views import map_view, equipment_view

urlpatterns = [
                    path('', home, name='home'),
                    path('admin/', admin.site.urls),
                    path('hotel/rooms/', rooms_list, name='rooms'),
                    path('hotel/rooms/booking/<int:room_id>/', rooms_booking, name='booking'),
                    path('hotel/rooms/booking/success/<int:room_id>/', rooms_success, name='success'),
                    path('hotel/rooms/booking/error/', rooms_booking, name='error'),
                    path('hotel/rooms/booking/pay/<int:room_id>/<int:booking_id>', rooms_pay, name='pay'),
                    path('hotel/rooms/booking/delete/<int:room_id>/<int:booking_id>', booking_delete, name='delete'),
                    path('hotel/about/', hotel_view, name='hotel'),
                    path('hotel/rooms/booking/show/', rooms_show, name='show'),
                    path('account/create/', sign_up_view, name='sign_up'),
                    path('account/login/', login_view, name='login'),
                    path('account/logout/', logout_view, name='logout'),
                    path('forecast/', forecast_view, name='forecast'),
                    path('ski/map/', map_view, name='map'),
                    path('ski/equipment/', equipment_view, name='equipment'),
              ]
