import json

import requests
from django.shortcuts import render


# Create your views here.
def forecast_view(request):
    city_name = 'Moscow'
    key = '9267d1b8d59eba39db7da5589e2c262d'
    response = requests.get(
        'https://api.openweathermap.org/data/2.5/forecast',
        params={
            'q': city_name, 'units': 'metric', 'lang': 'ru', 'appid': key
        })
    data = response.json()
    weather_tmp = []
    weather_lst = []
    for i in range(len(data['list'])):
        date = data['list'][i]['dt_txt']
        sky = data['list'][i]['weather'][0]['description']
        if len(weather_tmp) == 0:
            weather_tmp.append(date.split()[0])
        if date.split()[0] not in weather_tmp:
            weather_lst.append(weather_tmp)
            weather_tmp = [date.split()[0]]
        temp_evening = None
        temp_afternoon = None
        temp_morning = None
        temp_night = None
        if "06:00:00" in date and date.split()[0] in weather_tmp:
            temp_morning = round(data['list'][i]['main']['temp'])
            if temp_morning > 0:
                temp_morning = f'+{temp_morning}'
        if "12:00:00" in date and date.split()[0] in weather_tmp:
            temp_afternoon = round(data['list'][i]['main']['temp'])
            if temp_afternoon > 0:
                temp_afternoon = f'+{temp_afternoon}'
        if "18:00:00" in date and date.split()[0] in weather_tmp:
            temp_evening = round(data['list'][i]['main']['temp'])
            if temp_evening > 0:
                temp_evening = f'+{temp_evening}'
        if "00:00:00" in date and date.split()[0] in weather_tmp:
            temp_night = round(data['list'][i]['main']['temp'])
            if temp_night > 0:
                temp_night = f'+{temp_night}'
        if temp_night:
            weather_tmp.append(f'ночью температура: {temp_night}, на улице {sky}')
        if temp_morning:
            weather_tmp.append(f'утром температура: {temp_morning}, на улице {sky}')
        if temp_afternoon:
            weather_tmp.append(f'днем температура: {temp_afternoon}, на улице {sky}')
        if temp_evening:
            weather_tmp.append(f'вечером температура: {temp_evening}, на улице {sky}')
    return render(request, 'forecasts/forecast.html', {'weather': weather_lst})
