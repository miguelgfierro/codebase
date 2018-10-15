from flask import Flask, request, abort, jsonify, make_response


# HTML code
STATUS_OK = 200
NOT_FOUND = 404
BAD_REQUEST = 400
BAD_PARAM = 450


# app
app = Flask(__name__)


@app.route("/api/v1/post_json", methods=["POST"])
def post_status():
    """Post method
    Examples (not executable):
    In bash Linux/Mac, equivalent to:
    $ curl -X POST -d '{"param":"1"}' -H "Content-type: application/json" http://127.0.0.1:5000/api/v1/post_json
    In Windows, equivalent to:
    $ curl.exe -X POST -d '{\"param\":\"1\"}' -H "Content-type: application/json" http://127.0.0.1:5000/api/v1/post_json
    In Python, equivalent to:
    $ import requests, json
    $ headers = {"Content-type":"application/json"}
    $ data = {"param":"1"}
    $ res = requests.post("http://127.0.0.1:5000/api/v1/post_json", data=json.dumps(data), headers=headers)
    $ print(res.content)
    {
        "message": "Param = 1"
    }
    Examples:
        >>> import json
        >>> with app.test_client() as c:
        ...     headers = {"Content-type":"application/json"}
        ...     data = {"param":"1"}
        ...     rv = c.post("/api/v1/post_json", data=json.dumps(data), headers=headers)
        ...     status = rv.status
        ...     content = rv.get_data()
        >>> status
        '200 OK'

    """
    if not request.json or "param" not in request.json:
        abort(BAD_REQUEST)
    param = request.json["param"]
    resp = "Param = %s" % param
    return make_response(jsonify({"message": resp}), STATUS_OK)


@app.errorhandler(BAD_REQUEST)
def bad_request(error):
    """Custom bad request response
    Examples (not executable):
        $ import requests
        $ res = requests.post("http://127.0.0.1:5000/api/v1/post_json", data={"param":"2"})
        $ res.ok
        False
        $ res.json()
        {u"error": u"Bad request"}

    """
    return make_response(jsonify({"error": "Bad request"}), BAD_REQUEST)


@app.errorhandler(NOT_FOUND)
def not_found(error):
    """Custom not found response
    Examples (not executable):
        $ import requests
        $ res = requests.post("http://127.0.0.1:5000/api/v1/other", data={"other_param":"2"})
        $ res.ok
        False
        $ res.json()
        {u"error": u"Not found"}

    """
    return make_response(jsonify({"error": "Not found"}), NOT_FOUND)


if __name__ == "__main__":
    app.run(debug=True)
