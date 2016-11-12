import flask
app = flask.Flask(__name__)


@app.route("/")
def root():
    return flask.redirect("/api/1.0/current")


@app.route("/api/1.0/current")
def get_current():
    return "Hello, World"


if __name__ == "__main__":
    app.run()