import src.human_weather as human_weather


def get_current_at_location(owm, location):
    """
    get current weather for specified location
    Args:
        owm:    pyowm object
        location:   location to get weather

    Returns:
    String representation of current weather
    """
    observation = owm.weather_at_place(location)

    owm_location = observation.get_location()
    weather = observation.get_weather()

    temp = weather.get_temperature(unit='celsius')['temp']
    condition = weather.get_detailed_status()

    weather_str = "%s %s" % (human_weather.get_location(location), human_weather.get_human_representation(temp, condition))
    return weather_str

# def get_current_at_place_with_search(owm, place):
#     observations = owm.weather_at_places(place, 'like', 3)
#     if len(observations) > 0:
#         obs = observations[0]
#         return obs
#     else:
#         raise WeatherNotFoundException


# class WeatherNotFoundException(Exception):
#     def __init__(self, *args, **kwargs):
#         Exception.__init__(self, *args, **kwargs)
