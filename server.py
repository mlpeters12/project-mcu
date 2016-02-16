"""FINAL PROJECT."""

from jinja2 import StrictUndefined
from flask import Flask, render_template, redirect, request, flash, session
from model import Movie, connect_to_db, db
from flask_debugtoolbar import DebugToolbarExtension
import requests


app = Flask(__name__)

app.secret_key = "marvelpie"

app.jinja_env.undefined = StrictUndefined


@app.route("/")
def index():
    """Homepage."""

    return render_template("homepage.html")


@app.route("/movie_list")
def list_movies():
    """Return page showing all movies in the marvel cinematic universe"""


    movies = db.session.query(Movie.movie_name, Movie.movie_id, Movie.description, Movie.release_date, Movie.image).order_by(Movie.release_date).all()

    return render_template("movie_list.html", 
                            movies=movies)

@app.route("/movie/<int:movie_id>")
def show_movie(movie_id):
    """Return page showing the details of a selected movie.
    Show info about a movie.
    """
    
    print movie_name
    return render_template("movie_details.html")



if __name__ == "__main__":
    app.debug = True

    connect_to_db(app)

    DebugToolbarExtension(app)

    app.run()