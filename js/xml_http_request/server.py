# Attribution: https://gist.github.com/KentaYamada/2eed4af1f6b2adac5cc7c9063acf8720

from flask import Flask, request, render_template

app = Flask(__name__)
app.debug = True


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        return "Hello " + name
    # NOTE: index.html needs to be in a folder called templates
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
