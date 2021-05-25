from django.shortcuts import render


def map_view(request):
    return render(request, 'ski_resort/map.html', {})


def equipment_view(request):
    return render(request, 'ski_resort/equipment.html', {})
