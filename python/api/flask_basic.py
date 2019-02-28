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
    In bash, equivalent to:
    $ curl http://127.0.0.1:5000/hello
    $ curl http://127.0.0.1:5000/hello?name=Miguel
    In Python, equivalent to:
    $ import requests
    $ res = requests.get('http://127.0.0.1:5000/hello')
    $ res = requests.get('http://127.0.0.1:5000/hello?name=Miguel')
    
    Examples:
        >>> with app.test_client() as c:
        ...     rv = c.get('/hello')
        ...     status = rv.status
        ...     content = rv.data.decode('utf8')
        >>> status
        '200 OK'
        >>> content
        'Hello World!'
        >>> with app.test_client() as c:
        ...     rv = c.get('/hello?name=Miguel')
        ...     status = rv.status
        ...     content = rv.data.decode('utf8')
        >>> status
        '200 OK'
        >>> content
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
    In bash, equivalent to:
    $ curl http://127.0.0.1:5000/hello/5
    In Python, equivalent to:
    $ import requests
    $ res = requests.get('http://127.0.0.1:5000/hello/5')
    
    Examples:
        >>> with app.test_client() as c:
        ...     rv = c.get('/hello/5')    
        ...     status = rv.status
        ...     content = rv.data.decode('utf8')
        >>> status
        '200 OK'
        >>> content
        'Hello user 5'
        >>> with app.test_client() as c:
        ...     rv = c.get('/hello/10')    
        ...     status = rv.status
        ...     content = rv.json
        >>> status
        '450 UNKNOWN'
        >>> content
        {'message': 'User not found'}
    """
    if int(user_id) >= 10:
        raise InvalidUsage("User not found")
    else:
        return "Hello user " + user_id


class InvalidUsage(Exception):
    status_code = BAD_PARAM

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv["message"] = self.message
        return rv


@app.errorhandler(InvalidUsage)
def user_not_found(error):
    """Custom error handler.
    More info: http://flask.pocoo.org/docs/1.0/patterns/apierrors/#registering-an-error-handler
    """
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


if __name__ == "__main__":
    app.run(debug=True)
