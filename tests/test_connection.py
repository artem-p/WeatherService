from src.weather import weather
import responses
from src import strings

current_weather_query = weather.get_current_weather_url()


@responses.activate
def test_get_current_weather():
    responses.add(responses.GET, current_weather_query, body='{"error": "not found"}',
                  status=404, content_type='application/json')

    cur_weather = weather.get_current_weather()
    assert cur_weather == strings.resource_not_found