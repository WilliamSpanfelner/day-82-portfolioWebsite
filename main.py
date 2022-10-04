import random
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from datetime import date
from data import projects, links

app = Flask(__name__)
Bootstrap(app)
year = date.today().year


@app.route("/")
def about():
    # intro = "Hello, I'm William and this is my portfolio website."
    # print(len(intro))
    return render_template("index.html", links=links, yr=year)


@app.route("/portfolio")
def portfolio():
    # random.shuffle(projects)
    return render_template("portfolio.html", all_projects=projects, links=links, yr=year)


@app.route("/contact")
def contact():
    # TODO: Write the email code here.
    return render_template("contact.html", links=links, yr=year)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
