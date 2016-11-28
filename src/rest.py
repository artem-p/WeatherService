# -*- coding: utf-8 -*-
import flask
import json
import src.strings as strings
import pyowm
import src.secrets as secrets
import src.weather as weather
import pyowm.exceptions as pyowm_exceptions
import pyowm.exceptions.api_call_error
import pyowm.exceptions.api_response_error
import pyowm.exceptions.not_found_error
import pyowm.exceptions.parse_response_error
import pyowm.exceptions.unauthorized_error


current_weather_url = '/api/1.0/current'

app = flask.Flask(__name__)


def json_resp(code, data):
    return flask.Response(status=code, mimetype="application/json", response=json.dumps(data, ensure_ascii=False).encode('utf-8'))


@app.route("/")
def root():
    return flask.redirect(current_weather_url)


@app.route(current_weather_url)
def get_current():
    api_key = secrets.get("OWM_API_KEY")
    owm = pyowm.OWM(API_key=api_key, language="ru")

    place = "питер"

    try:
        cur_weather = weather.get_current_at_place(owm, place)

        return json_resp(200, cur_weather)

    except pyowm.exceptions.api_call_error.APICallError:
        return json_resp(502, {"error": "pyowm api call error"})
    except pyowm.exceptions.api_response_error.APIResponseError:
        return json_resp(502, {"error": "pyowm api response error"})
    except pyowm.exceptions.not_found_error.NotFoundError:
        return json_resp(502, {"error": "pyowm not found error"})
    except pyowm.exceptions.parse_response_error.ParseResponseError:
        return json_resp(502, {"error": "pyowm parse response error"})
    except pyowm.exceptions.unauthorized_error.UnauthorizedError:
        return json_resp(502, {"error": "pyowm unauthorized error"})
    except pyowm_exceptions.OWMError:
        return json_resp(502, {"error": "pyowm error"})

    # if current_weather['status'] is not None:
    #     if current_weather['status'] == weather.ok:
    #         return json_resp(200, {"current_weather_str": current_weather['text']})
    #     elif current_weather['status'] == weather.wunderground_not_available:
    #         return json_resp(502, {"error": strings.wunderground_not_available})
    #     elif current_weather['status'] == weather.wunderground_connection_error:
    #         return json_resp(502, {"error": strings.wunderground_error})
    #     elif current_weather['status'] == weather.bad_response_from_wunderground:
    #         return json_resp(500, {"error": strings.wunderground_bad_response})
    # else:
    #     pass


if __name__ == "__main__":
    app.run(debug=True)
