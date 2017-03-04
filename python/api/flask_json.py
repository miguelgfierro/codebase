from flask_app import app, STATUS_OK, BAD_REQUEST, NOT_FOUND
from flask import request, abort, jsonify, make_response, json


@app.errorhandler(BAD_REQUEST)
def bad_request(error):
    """Custom bad request response
    Examples:
        >>> import requests
        >>> res = requests.post('http://127.0.0.1:5000/api/v1/post_json', data={"param":"2"})
        >>> res.ok
        False
        >>> res.json()
        {u'error': u'Bad request'}

    """
    return make_response(jsonify({'error': 'Bad request'}), BAD_REQUEST)


@app.errorhandler(NOT_FOUND)
def not_found(error):
    """Custom not found response
    Examples:
        >>> import requests
        >>> res = requests.post('http://127.0.0.1:5000/api/v1/other', data={"other_param":"2"})
        >>> res.ok
        False
        >>> res.json()
        {u'error': u'Not found'}

    """
    return make_response(jsonify({'error': 'Not found'}), NOT_FOUND)


@app.route('/api/v1/post_json', methods=['POST'])
def post_status():
    """Post method
    Examples (executed in the command line in Linux/Mac):
        $ curl -X POST -d '{"param":"1"}' -H "Content-type: application/json" http://127.0.0.1:5000/api/v1/post_json
        In Windows:
        $ curl.exe -X POST -d "{\"param\":\"1\"}" -H "Content-type: application/json" http://127.0.0.1:5000/api/v1/post_json
        >>> import requests
        >>> headers = {'Content-type':'application/json'}
        >>> data = {"param":"1"}
        >>> res = requests.post('http://127.0.0.1:5000/api/v1/post_json', data=json.dumps(data), headers=headers)
        >>> print(res.content)
        {
          "message": "Param = 1"
        }

    """
    if not request.json or 'param' not in request.json:
        abort(BAD_REQUEST)
    param = request.json['param']
    resp = 'Param = %s' % param
    return make_response(jsonify({'message': resp}), STATUS_OK)



if __name__ == "__main__":
    app.run(debug=True)

