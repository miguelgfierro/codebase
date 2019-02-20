from flask import Flask, render_template

# app
app = Flask(__name__)
# define static folder for css, img, js
app.static_folder = "static"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/num/")
def num():
    num = 95
    return render_template("hello.html", number=num)


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
