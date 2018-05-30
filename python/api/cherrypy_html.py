from flask import Flask, render_template
import cherrypy
from paste.translogger import TransLogger


# app
app = Flask(__name__)
# define static folder for css, img, js
app.static_folder = 'static'


def run_server():
    # Enable WSGI access logging via Paste
    app_logged = TransLogger(app)

    # Mount the WSGI callable object (app) on the root directory
    cherrypy.tree.graft(app_logged, '/')

    # Set the configuration of the web server
    cherrypy.config.update({
        'engine.autoreload_on': True,
        'log.screen': True,
        'log.error_file': "cherrypy.log",
        'server.socket_port': 5000,
        'server.socket_host': '0.0.0.0',
        'server.thread_pool': 50,  # 10 is default
    })

    # Start the CherryPy WSGI web server
    cherrypy.engine.start()
    cherrypy.engine.block()


@app.route("/")
def index():
    return render_template('index.html')


if __name__ == "__main__":
    run_server()
