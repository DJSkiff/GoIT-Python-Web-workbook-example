"""https://goit.global/python-material-dev/docs/module-15/lesson-15-01#:~:text=%D0%9F%D0%BE%D1%82%D0%BE%D0%BC%20%D0%B4%D0%BE%D1%81%D1%82%D0%B0%D1%82%D0%BE%D1%87%D0%BD%D0%BE%20%D0%B4%D0%BE%D0%B1%D0%B0%D0%B2%D0%B8%D1%82%D1%8C%20endpoint%20%D0%B4%D0%BB%D1%8F%20%D0%B4%D0%BE%D0%BA%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D0%B0%D1%86%D0%B8%D0%B8%3A"""

from flask import Flask, jsonify
from flask_swagger import swagger

app = Flask(__name__)

@app.route("/spec")
def spec():
    return jsonify(swagger(app))

@app.route("/")
def index():
    """
        Flask Index Page
        ---
        responses:
          200:
            description: OK
        """
    return 'Hello World'


if __name__ == "__main__":
    Flask.run(app)