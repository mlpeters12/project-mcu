"""FINAL PROJECT."""

from jinja2 import StrictUndefined
from flask import Flask, render_template, redirect, request, flash, session
from model import Movie, Character, connect_to_db, db
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

@app.route("/movies/<int:movie_id>", methods=["GET"])
def show_movie(movie_id):
    """Return page showing the details of a selected movie.
    Show info about a movie.
    """

    movie_info = Movie.query.filter_by(movie_id=movie_id).one()
    
    return render_template("movie_details.html",
                            movie_info=movie_info)

@app.route("/characters")
def list_characters():
    """Return page showing all characters in the marvel cinematic universe"""


    characters = db.session.query(Character.character_id, Character.character_name, Character.civilian_name, Character.image1, Character.image2).all()

    return render_template("characters.html", 
                            characters=characters)

# @app.route("/movies/<int:movie_id>", methods=["GET"])
# def show_movie(movie_id):
#     """Return page showing the details of a selected movie.
#     Show info about a movie.
#     """

#     movie_info = Movie.query.filter_by(movie_id=movie_id).one()
    
#     return render_template("movie_details.html",
#                             movie_info=movie_info)

if __name__ == "__main__":
    app.debug = True

    connect_to_db(app)

    DebugToolbarExtension(app)

    app.run()