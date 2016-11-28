import pyowm
import src.secrets as secrets


def pyowm_try():
    api_key = secrets.get("OWM_API_KEY")
    owm = pyowm.OWM(api_key)

    observation = owm.weather_at_place("London, uk")
    w = observation.get_weather()
    print(w)
    pass


if __name__ == "__main__":
    pyowm_try()