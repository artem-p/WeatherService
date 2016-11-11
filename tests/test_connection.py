from src.weather import weather
import responses

current_weather_query = weather.get_current_weather_url()


@responses.activate
def test_get_current_weather():
    responses.add(responses.GET, current_weather_query, body='{"error": "not found"}',
                  status=404, content_type='application/json')
