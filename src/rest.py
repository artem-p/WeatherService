# -*- coding: utf-8 -*-
import flask
import json
from src.weather import weather
import src.strings as strings

current_weather_url = '/api/1.0/current'

app = flask.Flask(__name__)


def json_resp(code, data):
    return flask.Response(status=code, mimetype="application/json", response=json.dumps(data, ensure_ascii=False).encode('utf-8'))


@app.route("/")
def root():
    return flask.redirect("/api/1.0/current")


@app.route(current_weather_url)
def get_current():
    current_weather = weather.get_current_weather()

    if current_weather['status'] is not None:
        if current_weather['status'] == weather.ok:
            return json_resp(200, {"current_weather_str": current_weather['text']})
        elif current_weather['status'] == weather.wunderground_not_available:
            return json_resp(502, {"error": strings.wunderground_not_available})
        elif current_weather['status'] == weather.wunderground_connection_error:
            return json_resp(502, {"error": strings.wunderground_error})
        elif current_weather['status'] == weather.bad_response_from_wunderground:
            return json_resp(500, {"error": strings.wunderground_bad_response})
    else:
        pass

if __name__ == "__main__":
    app.run(debug=True)
