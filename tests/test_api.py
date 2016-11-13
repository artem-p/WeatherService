# -*- coding: utf-8 -*-
# http://flask.pocoo.org/docs/0.11/testing/

import src.rest as rest
import responses
from src.weather import weather

rest.app.config['TESTING'] = True
test_app = rest.app.test_client()
wunderground_current_weather_url = weather.get_current_weather_url()


def test_redirect():
    resp = test_app.get('/')
    assert resp.status_code == 302
    assert resp.location == 'http://localhost/api/1.0/current'
    pass


@responses.activate
def test_get_current():
    # mock response from wunderground
    mock_response_body = b'\n{\n  "response": {\n  "version":"0.1",\n  "termsofService":"http://www.wunderground.com/weather/api/d/terms.html",\n  "features": {\n  "conditions": 1\n  }\n\t}\n  ,\t"current_observation": {\n\t\t"image": {\n\t\t"url":"http://icons.wxug.com/graphics/wu2/logo_130x80.png",\n\t\t"title":"Weather Underground",\n\t\t"link":"http://www.wunderground.com"\n\t\t},\n\t\t"display_location": {\n\t\t"full":"\xd0\xa1\xd0\xb0\xd0\xbd\xd0\xba\xd1\x82-\xd0\x9f\xd0\xb5\xd1\x82\xd0\xb5\xd1\x80\xd0\xb1\xd1\x83\xd1\x80\xd0\xb3, Russia",\n\t\t"city":"\xd0\xa1\xd0\xb0\xd0\xbd\xd0\xba\xd1\x82-\xd0\x9f\xd0\xb5\xd1\x82\xd0\xb5\xd1\x80\xd0\xb1\xd1\x83\xd1\x80\xd0\xb3",\n\t\t"state":"",\n\t\t"state_name":"Russia",\n\t\t"country":"RS",\n\t\t"country_iso3166":"RU",\n\t\t"zip":"00000",\n\t\t"magic":"1",\n\t\t"wmo":"26063",\n\t\t"latitude":"59.97000122",\n\t\t"longitude":"30.25000000",\n\t\t"elevation":"6.1"\n\t\t},\n\t\t"observation_location": {\n\t\t"full":"St. Petersburg, ",\n\t\t"city":"St. Petersburg",\n\t\t"state":"",\n\t\t"country":"RS",\n\t\t"country_iso3166":"RU",\n\t\t"latitude":"59.79840088",\n\t\t"longitude":"30.26664925",\n\t\t"elevation":"75 ft"\n\t\t},\n\t\t"estimated": {\n\t\t},\n\t\t"station_id":"ULLI",\n\t\t"observation_time":"Last Updated on \xd0\x9d\xd0\xbe\xd1\x8f\xd0\xb1\xd1\x80\xd1\x8c 13, 9:30 PM MSK",\n\t\t"observation_time_rfc822":"Sun, 13 Nov 2016 21:30:00 +0300",\n\t\t"observation_epoch":"1479061800",\n\t\t"local_time_rfc822":"Sun, 13 Nov 2016 22:01:05 +0300",\n\t\t"local_epoch":"1479063665",\n\t\t"local_tz_short":"MSK",\n\t\t"local_tz_long":"Europe/Moscow",\n\t\t"local_tz_offset":"+0300",\n\t\t"weather":"\xd0\x9e\xd0\xb1\xd0\xbb\xd0\xb0\xd1\x87\xd0\xbd\xd0\xbe",\n\t\t"temperature_string":"25 F (-4 C)",\n\t\t"temp_f":25,\n\t\t"temp_c":-4,\n\t\t"relative_humidity":"93%",\n\t\t"wind_string":"From the West at 2 MPH",\n\t\t"wind_dir":"West",\n\t\t"wind_degrees":260,\n\t\t"wind_mph":2,\n\t\t"wind_gust_mph":0,\n\t\t"wind_kph":4,\n\t\t"wind_gust_kph":0,\n\t\t"pressure_mb":"1024",\n\t\t"pressure_in":"30.24",\n\t\t"pressure_trend":"0",\n\t\t"dewpoint_string":"23 F (-5 C)",\n\t\t"dewpoint_f":23,\n\t\t"dewpoint_c":-5,\n\t\t"heat_index_string":"NA",\n\t\t"heat_index_f":"NA",\n\t\t"heat_index_c":"NA",\n\t\t"windchill_string":"NA",\n\t\t"windchill_f":"NA",\n\t\t"windchill_c":"NA",\n\t\t"feelslike_string":"25 F (-4 C)",\n\t\t"feelslike_f":"25",\n\t\t"feelslike_c":"-4",\n\t\t"visibility_mi":"6.2",\n\t\t"visibility_km":"10.0",\n\t\t"solarradiation":"--",\n\t\t"UV":"0","precip_1hr_string":"-9999.00 in (-9999.00 mm)",\n\t\t"precip_1hr_in":"-9999.00",\n\t\t"precip_1hr_metric":"--",\n\t\t"precip_today_string":"0.00 in (0.0 mm)",\n\t\t"precip_today_in":"0.00",\n\t\t"precip_today_metric":"0.0",\n\t\t"icon":"mostlycloudy",\n\t\t"icon_url":"http://icons.wxug.com/i/c/k/nt_mostlycloudy.gif",\n\t\t"forecast_url":"http://www.wunderground.com/global/stations/26063.html",\n\t\t"history_url":"http://www.wunderground.com/history/airport/ULLI/2016/11/13/DailyHistory.html",\n\t\t"ob_url":"http://www.wunderground.com/cgi-bin/findweather/getForecast?query=59.79840088,30.26664925",\n\t\t"nowcast":""\n\t}\n}\n'
    responses.add(responses.GET, wunderground_current_weather_url, body=mock_response_body,
                  status=200, content_type='application/json')

    resp = test_app.get(rest.current_weather_url)
    assert resp.status_code == 200

    data_str = resp.data.decode("utf-8")

    # todo чтоб заработал assert + в заметку
    assert """Санкт-Петербург
13.11.2016 21:30
Облачно
Температура: -4 °C
Ощущается как: -4 °C
Ветер: З 1.1 м / с""" in data_str
