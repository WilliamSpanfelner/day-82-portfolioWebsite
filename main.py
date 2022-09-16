from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)


@app.route("/")
def home():
    # intro = "Hello, I'm William and this is my portfolio website."
    # print(len(intro))
    return render_template("index.html")


@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")


@app.route("/contact")
def contact():
    # TODO: Write the email code here.
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
