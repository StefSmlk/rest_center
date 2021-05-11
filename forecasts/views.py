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
    tmp_str = ''
    tmp_num = 0
    tmp_lst = ['collapse1', 'collapse2', 'collapse3', 'collapse4', 'collapse5', 'collapse6']
    weather_lst = []
    tmp_weather_lst = []
    date_lst = []
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
        wind_speed = round(data['list'][i]['wind']['speed'], 1)
        wind_dir = data['list'][i]['wind']['deg']
        date = data['list'][i]['dt_txt']
        sky = data['list'][i]['weather'][0]['description']
        temperature = round(data['list'][i]['main']['temp'])
        for j in range(len(wind_tmp_num)):
            if wind_dir in wind_tmp_num[j]:
                wind_dir = wind_tmp_str[j]
                break
        if temperature > 0:
            temperature = '+'+str(temperature)
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
        exist = any([date.split()[0] in days for days in date_lst])
        if not exist:
            if tmp_weather_lst:
                weather_lst.append(tmp_weather_lst)
            tmp_weather_lst = []
            tmp_num += 1
            tmp_str = 'collapse' + str(tmp_num)
            date_lst_tmp = [tmp_str]
            for k in tmp_lst:
                if k not in date_lst_tmp:
                    date_lst_tmp.append(k)
            date_lst_tmp.append(date.split()[0])
            date_lst.append(date_lst_tmp)
        tmp_weather_lst.append([tmp_str, date.split()[1], sky, temperature, temp, wind_speed, wind_dir])
    weather_lst.append(tmp_weather_lst)
    return render(request, 'forecasts/forecast.html', {'weather': weather_lst, 'date': date_lst})
