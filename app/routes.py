from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Eric'}
    posts = [
        {
            'author': {'username': 'Aleks'}, 
            'body': 'Hello! My name is Aleks!'
        },
        {
            'author': {'username': 'Ciara'}, 
            'body': 'Hello! My name is Ciara!'
        },
        {
            'author': {'username': 'Joel'}, 
            'body': 'Hello! My name is Joel!'
        }
    ]
    return render_template('index.html', title="Eric's Home page", user = user, posts=posts)
