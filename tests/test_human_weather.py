import src.human_weather as human_weather


def test_get_human_temp():
    f_temp = 0.3
    assert human_weather.get_temp(f_temp) == "около 0"

    f_temp = 0.0
    assert human_weather.get_temp(f_temp) == "около 0"

    f_temp = - 9.0
    assert human_weather.get_temp(f_temp) == "минус 9"

    f_temp = -14.9
    assert human_weather.get_temp(f_temp) == "минус 15"

    f_temp = -14.4
    assert human_weather.get_temp(f_temp) == "минус 14"

    f_temp = 4.4
    assert human_weather.get_temp(f_temp) == "плюс 4"

    f_temp = 1.0
    assert human_weather.get_temp(f_temp) == "плюс 1"

    f_temp = 2.7
    assert human_weather.get_temp(f_temp) == "плюс 3"

    f_temp = 2.4
    assert human_weather.get_temp(f_temp) == "плюс 2"

    f_temp = 5.4
    assert human_weather.get_temp(f_temp) == "5 градусов"

    f_temp = 8.9
    assert human_weather.get_temp(f_temp) == "9 градусов"

    f_temp = 10.4
    assert human_weather.get_temp(f_temp) == "10 градусов"

    f_temp = 14.4
    assert human_weather.get_temp(f_temp) == "14 градусов"

    f_temp = 15.4
    assert human_weather.get_temp(f_temp) == "плюс 15"

    f_temp = 19.6
    assert human_weather.get_temp(f_temp) == "плюс 20"


def test_get_human_location():
    location_from_query = "Питер"
    assert human_weather.get_location(location_from_query) == "В Питер"

    location_from_query = "москва"
    assert human_weather.get_location(location_from_query) == "В Москва"

    location_from_query = "лондон"
    assert human_weather.get_location(location_from_query) == "В Лондон"
