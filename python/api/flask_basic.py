from flask_app import app, BAD_PARAM
from flask import request, json, jsonify, abort, make_response
import werkzeug.exceptions as ex


@app.route('/hello')
def hello_world():
    """Basic endpoint with arguments.
    Examples:
        Equivalent to:
        $ curl http://127.0.0.1:5000/hello
        $ curl http://127.0.0.1:5000/hello?name=Miguel
        >>> import requests
        >>> res = requests.get('http://127.0.0.1:5000/hello')
        >>> print(res.ok)
        True
        >>> print(res.content)
        Hello World!
        >>> res = requests.get('http://127.0.0.1:5000/hello?name=Miguel')
        >>> print(res.ok)
        True
        >>> print(res.content)
        Hello Miguel

    """
    if 'name' in request.args:
        return "Hello " + request.args['name']
    else:
        return "Hello World!"


@app.route('/hello/<user_id>')
def hello_user(user_id):
    """Basic endpoint with url parameters.
    Parameters:
        user_id (str): String parameter.
    Examples:
        $ curl http://127.0.0.1:5000/hello/5
        >>> import requests
        >>> res = requests.get('http://127.0.0.1:5000/hello/5')
        >>> print(res.ok)
        True
        >>> print(res.content)
        Hello user 5
        >>> res = requests.get('http://127.0.0.1:5000/hello/10')
        >>> print(res.ok)
        False
        >>> print(res.content)
        {
          "error": "User not found",
          "status": 450
        }

    """
    if int(user_id) >= 10:
        abort(BAD_PARAM)
        #user_not_found()
    else:
        return "Hello user " + user_id


class CustomBadParam(ex.HTTPException):
    """Support class for being able to call `abort(BAD_PARAM)` instead of `user_not_found()`."""
    code = BAD_PARAM
    description = '<p>Bad parameter</p>'
abort.mapping[BAD_PARAM] = CustomBadParam


@app.errorhandler(BAD_PARAM)
def user_not_found(error=None):
    """Custom error handler."""
    return make_response(jsonify({'status': BAD_PARAM,
                                  'error': 'User not found'}), BAD_PARAM)


if __name__ == "__main__":
    app.run(debug=True)
