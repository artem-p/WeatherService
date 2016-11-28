def get_current_at_place(owm, place):
    observation = owm.weather_at_place(place)

    location = observation.get_location()
    weather = observation.get_weather()

    weather_str = "%s %s %s" % (location.get_name(), str(weather.get_temperature(unit='celsius')['temp']),
                                weather.get_detailed_status())
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
