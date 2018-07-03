# The WebSocket protocol enables interaction between a web client and a web
# server with lower overheads, facilitating real-time data transfer from and
# to the server. This is made possible by providing a standardized way for the
# server to send content to the client without being first requested by the
# client, and allowing messages to be passed back and forth while keeping the
# connection open.
# +info: https://en.wikipedia.org/wiki/WebSocket
# https://github.com/miguelgrinberg/Flask-SocketIO/tree/master/example

from flask import Flask, render_template
from flask_socketio import SocketIO, emit, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('websocket.html')


# @socketio.on('client_connected')
# def handle_client_connect_event(json):
#     print('received json from client: {0}'.format(str(json)))

@socketio.on('connect')
def test_connect():
    print('Client connected')


@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')


# Receives my_pong from the client and sends my_pong from the server
@socketio.on('my_ping')
def ping_pong():
    emit('my_pong')

# @socketio.on('message')
# def handle_json_button(json):
#     print('received json from client: {0}'.format(str(json)))
#     return_json = {}
#     return_json['stuff I heard you say'] = json
#     send(return_json, json=True)
# @socketio.on('message')
# def handle_json_button(json):
#     # it will forward the json to all clients.
#     send(json, json=True)


# @socketio.on('alert_button')
# def handle_alert_event(json):
#     # it will forward the json to all clients.
#     print('Message from Javascript client: {0}'.format(json))
#     emit('alert', 'I see you pushed the ALERT button.')
# @socketio.on('alert_button')
# def handle_alert_event(json):
#     # it will forward the json to all clients.
#     print('Message from client was {0}'.format(json))
#     emit('alert', 'Message from backend')

# @socketio.on('my event')                          # Decorator to catch an event called "my event":
# def test_message(message):                        # test_message() is the event callback function.
#     emit('my response', {'data': 'got it!'})      # Trigger a new event called "my response"
#                                                   # that can be caught by another callback later in the program.


if __name__ == '__main__':
    socketio.run(app)
