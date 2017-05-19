# -*- coding: UTF-8 -*-
from app import app
from flask import  render_template
@app.route('/')
@app.route('/index')
def index():
    user = {'nickname' : 'Miguel'}
    posts=[
        {
            'author': { 'nickname': 'John' },
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': { 'nickname': 'Susan' },
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index.html",title='home', user=user,posts=posts)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html',
        title = 'Sign In',
        form = form)