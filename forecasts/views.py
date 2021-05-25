import requests
from django.shortcuts import render


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
    weather_lst = []
    tmp_weather_lst = []
    date_lst = []
    tmp_lst = ['collapse1', 'collapse2', 'collapse3', 'collapse4', 'collapse5', 'collapse6']
    tmp_months = [
        'января',
        'февраля',
        'марта',
        'апреля',
        'мая',
        'июня',
        'июля',
        'августа',
        'сентября',
        'октября',
        'ноября',
        'декабря',
    ]
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
        wind_direction = data['list'][i]['wind']['deg']
        date = data['list'][i]['dt_txt']
        sky = data['list'][i]['weather'][0]['description']
        temperature = round(data['list'][i]['main']['temp'])
        for j in range(len(wind_tmp_num)):  # change wind direction in degrees to text
            if wind_direction in wind_tmp_num[j]:
                wind_direction = wind_tmp_str[j]
                break
        if temperature > 0:  # add '+' to temperature value
            temperature = '+' + str(temperature)
        if 'облачно' in sky:  # add gif icon in depend on weather
            temp = 'rest_center/111.svg'
        if 'ясно' in sky:
            temp = 'rest_center/112.svg'
        if 'дождь' in sky:
            temp = 'rest_center/113.svg'
        if 'пасмурно' in sky:
            temp = 'rest_center/114.svg'
        if 'снег' in sky:
            temp = 'rest_center/115.svg'
        if 'гроза' in sky:
            temp = 'rest_center/116.svg'
        exist = any([date.split()[0] in days for days in date_lst])  # add new date if it not exists in list
        if not exist:
            if tmp_weather_lst:
                while len(tmp_weather_lst) < 8:
                    tmp_weather_lst.append([])
                weather_lst.append(tmp_weather_lst)
            tmp_weather_lst = []
            tmp_num += 1
            tmp_str = 'collapse' + str(tmp_num)  # make class for js working
            date_lst_tmp = [tmp_str]
            for k in tmp_lst:
                if k not in date_lst_tmp:
                    date_lst_tmp.append(k)
            date_lst_tmp.append(date.split()[0])
            date_lst.append(date_lst_tmp)  # create list of dates
        tmp_weather_lst.append(
            [tmp_str, date.split()[1], sky, temperature, temp, wind_speed, wind_direction]
        )  # create weather list
    while len(tmp_weather_lst) < 8:  # make all lists the same length
        tmp_weather_lst.append([])
    weather_lst.append(tmp_weather_lst)  # create main weather list
    for part in date_lst:  # make list of dates better
        parts = part[6].split('-')
        part.pop()
        parts[1] = tmp_months[int(parts[1]) - 1]  # convert month integer into text
        part.append(parts)
    return render(request, 'forecasts/forecast.html', {'weather': weather_lst, 'date': date_lst})
