# -*- coding: utf-8 -*-
import datetime

import requests
import src.secrets as secrests
from src.weather import wind
from src import strings

ok = 1
wunderground_not_available = -1
wunderground_connection_error = -2
bad_response_from_wunderground = -3

class CurrentWeather:
    def __init__(self, current_weather_json):
        self.json_weather = current_weather_json

    def parse(self):
        # parse response result
        self.city = None
        self.time = None
        self.conditions = None
        self.temp = None
        self.feelslike = None
        self.wind_dir = None
        self.wind_kph = None

        if self.json_weather:
            current_observation = self.json_weather['current_observation']
            self.city = current_observation['display_location']['city']
            timestamp = int(current_observation['observation_epoch'])
            self.time = time_str_from_epoch(timestamp)
            self.conditions = current_observation['weather']
            self.temp = current_observation['temp_c']
            self.feelslike = int(current_observation['feelslike_c'])
            self.wind_dir = current_observation['wind_degrees']
            self.wind_kph = current_observation['wind_kph']

    def to_text(self):
        # Преобразуем в текст для вывода
        self.parse()
        self.wind = wind.Wind(self.wind_kph, self.wind_dir)
        textPart = """%s
%s
%s
Температура: %d °C
Ощущается как: %d °C
Ветер: """ % (self.city, self.time, self.conditions, self.temp, self.feelslike)
        text = textPart + self.wind.to_text()
        return text


def get_current_weather_url():
    """
    make query with current weather request

    """
    api_key = secrests.get("WUNDERGROUND_API_KEY")
    query = "http://api.wunderground.com/api/%s/conditions/lang:RU/q/Russia/St_Petersburg.json" % api_key
    return query


def get_current_weather():
    """
    Returns: text representation of current weather condition

    """

    query = get_current_weather_url()
    output = {'status': None, 'text': ""}
    current_weather_response = requests.get(query)

    if current_weather_response.ok:
        response_json = current_weather_response.json()
        if 'response' in response_json and not 'error' in response_json['response']:
            current_weather = CurrentWeather(response_json)
            output['status'] = ok
            output['text'] = current_weather.to_text()
        else:
            output['status'] = bad_response_from_wunderground
            output['text'] = strings.wunderground_bad_response
    else:
        if current_weather_response.status_code == 404:
            # wundergroung not available
            output['status'] = wunderground_not_available
            output['text'] = strings.wunderground_not_available
        else:
            # another wunderground error
            output['status'] = wunderground_connection_error
            output['text'] = strings.wunderground_error

    return output


def time_str_from_epoch(time_epoch):
    time_from_epoch = datetime.datetime.fromtimestamp(time_epoch)
    return time_from_epoch.strftime("%d.%m.%Y %H:%M")


# Сделать из метки нормальное время с юнит-тестом
# "observation_epoch":"1462644000",
# "observation_time_rfc822":"Sat, 07 May 2016 21:00:00 +0300",

# Прогноз
# forecast_response = requests.get('http://api.wunderground.com/api/67baf1d645fb0443/forecast/q/Russia/St_Petersburg.json')
# forecast_response.text

# result = forecast_response.json()
# forecasts = result['forecast']
# simple_forecast = forecasts['simpleforecast']
# days_forecast = simple_forecast['forecastday']

# for day_forecast in days_forecast:
#   year = day_forecast['date']['year']
#   month = day_forecast['date']['month']

# year
