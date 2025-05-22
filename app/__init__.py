from flask import Flask
from flask import render_template
from flask import redirect
from random import randint

app = Flask(__name__)

@app.get("/")
def home():
    return render_template("pages/home.jinja")

@app.get("/about/")
def about():
    return render_template("pages/about.jinja")

@app.get("/random/")
def random():
    rand_num = (randint(1,1000000))
    return render_template('pages/rng.jinja', number = rand_num)

@app.get("/number/<int:num>")
def analyse_number(num):
    print(f"you entered: {num}")
    return render_template('pages/number.jinja', number = num)

@app.get("/form/")
def form():
    return render_template("pages/form.jinja")

@app.get("/secret/")
def secret():
    return render_template("pages/secret.jinja")


@app.errorhandler(404)
def notfound(e):
    return render_template("pages/404.jinja")