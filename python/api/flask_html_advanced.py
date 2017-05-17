from flask_app import app
from flask import render_template


@app.route("/")
def index():
	num = 95
    return render_template('hello.html', number=num)


if __name__ == "__main__":
    app.run(debug=True)
