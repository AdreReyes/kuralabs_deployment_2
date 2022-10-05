from application import app

# def test_quick():
#   a = "jeff"
#   greeting = greet(a)
#   assert greeting == "Hi jeff"

def test_home_page():
    response = app.test_client().get('/')
    assert response.status_code == 200
    
from flask import Flask, redirect, url_for, render_template 

app = Flask(_name_)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    return render_template()

@app.route("/<user>")
def user(usr):
    return f"<h1>{usr}</h1>"

if _name_ == "_main_"
