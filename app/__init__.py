from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from random import randint

# Create the app.
app = Flask(__name__)

# Home page - loading a static page.
@app.get("/")
def home():
    client = connect_db()
    result = client.execute("SELECT * FROM things")
    print(result.rows)
    return render_template("pages/home.jinja")

# About page - loading a static page.
@app.get("/about/")
def about():
    return render_template("pages/about.jinja")

# Random number page - passing a value into the template.
@app.get("/random/")
def random():
    rand_num = (randint(1,1000000))
    return render_template('pages/rng.jinja', number = rand_num)

# Number page - getting a value from route and passing it into template.
@app.get("/number/<int:num>")
def analyse_number(num):
    print(f"you entered: {num}")
    return render_template('pages/number.jinja', number = num)

# Form page - Static page with a form.
@app.get("/form/")
def form():
    return render_template("pages/form.jinja")

# Secret page - loading a static page.
@app.get("/secret/")
def secret():
    return render_template("pages/secret.jinja")

# Error page - Handle any errors.
@app.errorhandler(404)
def notfound(e):
    return render_template("pages/404.jinja")

# Handle data posted from the form.
@app.post("/process_form")
def process_form():
    print(f"Form data: ${request.form}")
    return render_template(
        "pages/form_data.jinja",
        name = request.form["name"],
        age = request.form["age"],
        character = request.form["character"]
        )