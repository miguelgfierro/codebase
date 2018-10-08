from flask import request, jsonify, abort, make_response, Flask
import werkzeug.exceptions as ex


# HTML code
STATUS_OK = 200
NOT_FOUND = 404
BAD_REQUEST = 400
BAD_PARAM = 450


# app
app = Flask(__name__)


@app.route("/hello")
def hello_world():
    """Basic endpoint with arguments.
    Examples (not executable):
        Equivalent to:
        $ curl http://127.0.0.1:5000/hello
        $ curl http://127.0.0.1:5000/hello?name=Miguel
        $ import requests
        $ res = requests.get('http://127.0.0.1:5000/hello')
        $ res.ok
        True
        $ res.content
        'Hello World!'
        $ res = requests.get('http://127.0.0.1:5000/hello?name=Miguel')
        $ res.ok
        True
        $ res.content
        'Hello Miguel'

    """
    if "name" in request.args:
        return "Hello " + request.args["name"]
    else:
        return "Hello World!"


@app.route("/hello/<user_id>")
def hello_user(user_id):
    """Basic endpoint with url parameters.
    Args:
        user_id (str): String parameter.
    Examples (not executable):
        $ curl http://127.0.0.1:5000/hello/5
        $ import requests, subprocess
        $ proc = subprocess.run(["python", "python/api/flask_basic.py"], timeout=10) 
        $ res = requests.get('http://127.0.0.1:5000/hello/5')
        $ res.ok
        True
        $ res.content
        'Hello user 5'
        $ res = requests.get('http://127.0.0.1:5000/hello/10')
        $ res.ok
        False
        $ print(res.content)
        {
          "error": "User not found",
          "status": 450
        }

    """
    if int(user_id) >= 10:
        user_not_found()
    else:
        return "Hello user " + user_id


@app.errorhandler(ex.BadRequest)
def user_not_found(e):
    """Custom error handler."""
    return make_response(
        jsonify({"status": BAD_PARAM, "error": "User not found"}), BAD_PARAM
    )


if __name__ == "__main__":
    app.run(debug=True)
