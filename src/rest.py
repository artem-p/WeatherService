import flask
import json
from src.weather import weather


app = flask.Flask(__name__)


def json_resp(code, data):
    return flask.Response(status=code, mimetype="application/json", response=json.dumps(data) + "\n")


@app.route("/")
def root():
    return flask.redirect("/api/1.0/current")


@app.route("/api/1.0/current")
def get_current():
    current_weather = weather.get_current_weather()
    return json_resp(200, {"current_weather_str": current_weather})


if __name__ == "__main__":
    app.run(debug=True)
