def get_human_representation(temp, weather_condition):
    """
    get weather in human readable representation
    Args:
        temp:
        weather_condition:

    Returns:
    str
    """
    return "%s %s" % (str(temp), weather_condition)


def get_temp(f_temp):
    """
    get human representation of temperature
    Args:
        f_temp: float temp value from owm

    Returns:
    str
    """

    temp_output = str(f_temp)
    round_temp = round(f_temp)

    minus_format = 'минус %d'
    plus_format = 'плюс %d'
    grad_format = '%d градусов'

    if 0 <= round_temp < 1:
        temp_output = "около 0"
    elif round_temp < 0:
        temp_output = minus_format % abs(round_temp)
    elif round_temp <= 4:
        temp_output = plus_format % round_temp
    elif round_temp <= 14:
        temp_output = grad_format % round_temp

    return temp_output
