from flask import Flask


app = Flask(__name__)


@app.route("/")
def home():
    return "Go away"


@app.route("/user")
def user():
    return "Go away, smelly-face!"


if __name__ == "__main__":
    app.run(debug=True)