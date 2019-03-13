#!/usr/bin/env python
from models import *
from trending import *
from movies import *
from shows import *
from single import *
from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from functools import wraps

app = Flask(__name__,
            static_url_path='',
            static_folder='web/static',
            template_folder='web/templates')

# Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123'
app.config['MYSQL_DB'] = 'movies'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
# init MYSQL
mysql = MySQL(app)


# Index
@app.route('/')
def index():
    return render_template('home.html')


# Movies
@app.route('/filmi/<string:page>/', methods=['GET', 'POST'])
def movies(page):
    if request.method == "GET":

        # Check movies.py for function
        vsi = get_movies(page)

        # Check trending.py for function
        trending = get_trending()

        return render_template("movies.html", trending=trending, vsi=vsi, page=page)

    elif request.method == "POST":
        paging = request.form

        if "prejsna-stran" in paging:
            if int(page) == 1:
                page = 1
            else:
                page = int(page) - 1
        elif "naslednja-stran" in paging:
            page = int(page) + 1

        return redirect("/filmi/" + str(page))


# Shows
@app.route('/oddaje/<string:page>/', methods=['GET', 'POST'])
def shows(page):
    if request.method == "GET":

        # Check movies.py for function
        vsi = get_shows(page)

        # Check trending.py for function
        trending = get_trending()

        return render_template("shows.html", trending=trending, vsi=vsi, page=page)

    elif request.method == "POST":
        paging = request.form

        if "prejsna-stran" in paging:
            if int(page) == 1:
                page = 1
            else:
                page = int(page) - 1
        elif "naslednja-stran" in paging:
            page = int(page) + 1

        return redirect("/oddaje/" + str(page))


# Single Movie
@app.route('/film/<string:id>/')
def single_movie(id):

    single = get_single_movie(id)

    return render_template('single_movie.html', single=single)


# Single Show
@app.route('/oddaja/<string:id>/')
def single_show(id):

    single = get_single_show(id)

    return render_template('single_show.html', single=single)


# Movie Category
@app.route('/kategorija/filmi/<string:category>/stran/<string:page>/', methods=['GET', 'POST'])
def movie_category(category, page):
    if request.method == "GET":

        # Check movies.py for function
        vsi = get_movie_category(category, page)

        # Check trending.py for function
        trending = get_trending()

        return render_template("movie_category.html", trending=trending, vsi=vsi, page=page)

    elif request.method == "POST":
        paging = request.form

        if "prejsna-stran" in paging:
            if int(page) == 1:
                page = 1
            else:
                page = int(page) - 1
        elif "naslednja-stran" in paging:
            page = int(page) + 1

        return redirect("/kategorija/filmi/" + str(category) + "/stran/" + str(page))


# Show Category
@app.route('/kategorija/oddaje/<string:category>/stran/<string:page>/', methods=['GET', 'POST'])
def show_category(category, page):
    if request.method == "GET":

        # Check shows.py for function
        vsi = get_show_category(category, page)

        # Check trending.py for function
        trending = get_trending()

        return render_template("show_category.html", trending=trending, vsi=vsi, page=page)

    elif request.method == "POST":
        paging = request.form

        if "prejsna-stran" in paging:
            if int(page) == 1:
                page = 1
            else:
                page = int(page) - 1
        elif "naslednja-stran" in paging:
            page = int(page) + 1

        return redirect("/kategorija/oddaje/" + str(category) + "/stran/" + str(page))


# Favorites
@app.route('/priljubljeno/')
def favorites():
    return render_template('favorites.html')


if __name__ == '__main__':
    app.secret_key = 'secret123'
    app.run()
