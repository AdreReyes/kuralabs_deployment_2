from application import app
from flask import Flask
from flask import request


# def test_quick():
#   a = "jeff"
#   greeting = greet(a)
#   assert greeting == "Hi jeff"

def test_home_page():
    response = app.test_client().get('/')
    assert response.status_code == 200
    print("Done.")
    
@app.route('/users/url-shortener', methods = ['POST'])
def user(user_id):
    if request.method == 'POST':
        """modify/update the information for url-shortener"""
        data = request.form # a multidict containing POST data
