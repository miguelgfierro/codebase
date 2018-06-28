# The WebSocket protocol enables interaction between a web client and a web
# server with lower overheads, facilitating real-time data transfer from and
# to the server. This is made possible by providing a standardized way for the
# server to send content to the client without being first requested by the
# client, and allowing messages to be passed back and forth while keeping the
# connection open.
# source: https://en.wikipedia.org/wiki/WebSocket

from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)
