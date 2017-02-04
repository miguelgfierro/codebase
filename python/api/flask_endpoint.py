from flask_app import *
from flask import request, abort, jsonify, make_response


@app.route('/api/v1/status',methods=['POST'])
def status():
    if not request.json:
        abort(BAD_REQUEST)
    resp = 'Status OK'
    return make_response(jsonify({'message': resp}), STATUS_OK)
