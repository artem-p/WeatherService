import pyowm
import src.secrets as secrets
import src.weather as weather
import pyowm.exceptions as pyowm_exceptions

if __name__ == "__main__":
    api_key = secrets.get("OWM_API_KEY")
    owm = pyowm.OWM(API_key=api_key, language="ru")

    place = "питер"

    try:
        cur_weather = weather.get_current_at_location(owm, place)

        print(cur_weather)
    except pyowm.exceptions.OWMError:
        print("Ошибка pyowm")
    # except weather.WeatherNotFoundException:
    #     print("Не удалось получить данные для указанного места")
