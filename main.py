from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)


@app.route("/")
def home():
    return render_template("base.html")


@app.route("/user")
def user():
    return "Go away, smelly-face!"


if __name__ == "__main__":
    app.run(debug=True)
