# The WebSocket protocol enables interaction between a web client and a web
# server with lower overheads, facilitating real-time data transfer from and
# to the server. This is made possible by providing a standardized way for the
# server to send content to the client without being first requested by the
# client, and allowing messages to be passed back and forth while keeping the
# connection open.
# +info: https://en.wikipedia.org/wiki/WebSocket
# https://github.com/miguelgrinberg/Flask-SocketIO/tree/master/example
# https://www.shanelynn.ie/asynchronous-updates-to-a-webpage-with-flask-and-socket-io/

from flask import Flask, render_template, make_response, jsonify
from flask_socketio import SocketIO, emit

# HTML code
STATUS_OK = 200


app = Flask(__name__)
app.config["SECRET_KEY"] = "secret!"
socketio = SocketIO(app)


@app.route("/")
def index():
    """To access the main page, go to http://localhost:5000"""
    return render_template("websocket.html")


@socketio.on("connect")
def test_connect():
    print("Client connected")


@socketio.on("disconnect")
def test_disconnect():
    print("Client disconnected")


@socketio.on("my_event")
def test_message(message):
    """Receives a message from the client and sends a response.
    If the system is using a namespace, the decorator would be:
    @socketio.on('my_event', namespace='/test').
    In the client, the message is sent through a form that in JS is handeled
    with the tag 'my_event'. When broadcast=True, the message is sent to all
    connected clients, if False, only to the first one connected.
    """
    received_message = message["data"]
    print("The server received the message: {}".format(received_message))
    new_response = received_message + " Oh Yeah!"
    emit(
        "my_response",
        {"data": new_response, "note": "Message improved"},
        broadcast=False,
    )


@socketio.on("my_ping")
def ping_pong():
    """Receives my_pong from the client and sends my_pong from the server"""
    emit("my_pong")


@app.route("/health")
def health_check():
    """This is a health end point, we can make a GET call to the api and
    the websocket will emit a response that will be visible in the web page.
    To do it, first open a browser and type http://localhost:5000, then in
    a terminal type: curl http://localhost:5000/health. If you go back to
    the browser, you will see that there is a new message that has been sent
    from the server, as a response to the client query in /health end point.
    Note: when using a standard flask end point, we can't use emit directly,
    we need to use socketio.emit.
    More info: https://github.com/miguelgrinberg/Flask-SocketIO/issues/40
    Note 2: if the system is using a namespace, we have to add an extra
    argument to socketio.emit(..., namespace='/test').
    """
    socketio.emit("my_response", {"data": "HEALTH CHECK", "note": "OK"}, broadcast=True)
    return make_response(jsonify({"health": "OK"}), STATUS_OK)


if __name__ == "__main__":
    socketio.run(app, debug=False)
