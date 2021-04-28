from django.shortcuts import render

from ski_resort.models import SkiRentModel, BoardRentModel, BootsRentModel


def map_view(request):
    return render(request, 'ski_resort/map.html')


def equipment_view(request):
    return render(request, 'ski_resort/equipment.html', )


def boards_view(request):
    context = SkiRentModel.objects
    return render(request, 'ski_resort/board.html', {'context': context})


def skis_view(request):
    context = BoardRentModel.objects
    return render(request, 'ski_resort/skis.html', {'context': context})


def boots_view(request):
    context = BootsRentModel.objects
    return render(request, 'ski_resort/boots.html', {'context': context})
