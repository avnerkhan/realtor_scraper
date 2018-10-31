from flask import Flask
from flask_cors import CORS


app = Flask(__name__)


@app.route("/")
def test():
    return "testing works"


if __name__ == "__main__":
    app.run()
