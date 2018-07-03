# The WebSocket protocol enables interaction between a web client and a web
# server with lower overheads, facilitating real-time data transfer from and
# to the server. This is made possible by providing a standardized way for the
# server to send content to the client without being first requested by the
# client, and allowing messages to be passed back and forth while keeping the
# connection open.
# +info: https://en.wikipedia.org/wiki/WebSocket
# https://github.com/miguelgrinberg/Flask-SocketIO/tree/master/example
# https://www.shanelynn.ie/asynchronous-updates-to-a-webpage-with-flask-and-socket-io/

from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('websocket.html')


@socketio.on('connect')
def test_connect():
    print('Client connected')


@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')


# Receives a message from the client and sends a response.
# If the system is using a namespace, the decorator would be:
# @socketio.on('my_event', namespace='/test').
# In the client, the message is sent through a form that in JS is handeled
# with the tag 'my_event'. When broadcast=True, the message is sent to all
# connected clients, if False, only to the first one connected.
@socketio.on('my_event') 
def test_message(message):
    received_message = message['data']
    print("The server received the message: {}".format(received_message))
    new_response = received_message + ' Oh Yeah!'
    emit('my_response',
         {'data': new_response, 'note': 'Message improved'},
         broadcast=False)


# Receives my_pong from the client and sends my_pong from the server
@socketio.on('my_ping')
def ping_pong():
    emit('my_pong')


if __name__ == '__main__':
    socketio.run(app, debug=False)
