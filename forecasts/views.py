import json

import requests
from django.shortcuts import render
from django.utils.safestring import mark_safe


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
    temp = ''
    weather_lst = []
    wind_tmp_str = [
        'восточный',
        'северо-восточный',
        'северный',
        'северо-западный',
        'западный',
        'юго-западный',
        'южный',
        'юго-восточный',
        'восточный'
    ]
    wind_tmp_num = [
        list(range(0, 23)),
        list(range(23, 68)),
        list(range(69, 113)),
        list(range(114, 158)),
        list(range(159, 203)),
        list(range(204, 248)),
        list(range(249, 293)),
        list(range(293, 338)),
        list(range(339, 361))
    ]
    for i in range(len(data['list'])):
        num = -1
        wind_speed = data['list'][i]['wind']['speed']
        wind_dir = data['list'][i]['wind']['deg']
        date = data['list'][i]['dt_txt']
        sky = data['list'][i]['weather'][0]['description']
        temperature = round(data['list'][i]['main']['temp'])
        if temperature > 0:
            temperature = '+'+str(temperature)
        for nums in wind_tmp_num:
            if wind_dir not in nums:
                num += 1
            else:
                break
        wind_dir = wind_tmp_str[num]
        if 'облачно' in sky:
            temp = mark_safe('&#9925;')
        if 'ясно' in sky:
            temp = mark_safe('&#9728;')
        if 'дождь' in sky:
            temp = mark_safe('&#9926;')
        if 'пасмурно' in sky:
            temp = mark_safe('&#9729;')
        if 'снег' in sky:
            temp = mark_safe('&#10052;')
        if 'гроза' in sky:
            temp = mark_safe('&#9928;')
        exist = any([date.split()[0] in days for days in weather_lst])
        if exist:
            weather_lst.append([date.split()[1], sky, temperature, temp, wind_speed, wind_dir])
        else:
            weather_lst.append([date.split()[1], sky, temperature, temp, wind_speed, wind_dir, date.split()[0]])

    return render(request, 'forecasts/forecast.html', {'weather': weather_lst})
