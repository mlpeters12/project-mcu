"""FINAL PROJECT."""

from jinja2 import StrictUndefined
from flask import Flask, render_template, redirect, request, flash, session, jsonify
from model import Movie, Character, MovieCharacter, Affiliation, CharacterAffiliation, connect_to_db, db
from flask_debugtoolbar import DebugToolbarExtension
import requests
import json


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


    movies = Movie.query.order_by(Movie.release_date).all()

    return render_template("movie_list.html", 
                            movies=movies)

# @app.route("/affiliations")
# def list_affiliations():
#     """Return page showing all relationshuip in the marvel cinematic universe"""
    

#     return render_template("/index.html")

@app.route("/movies/<int:movie_id>", methods=["GET"])
def show_movie(movie_id):
    """Return page showing the details of a selected movie.
    Show info about a movie.
    """

    movie_info = Movie.query.filter_by(movie_id=movie_id).one()
    movie_char = movie_info.characters
    

    return render_template("movie_details.html",
                            movie_info=movie_info,
                            movie_char=movie_char)

@app.route("/characters")
def list_characters():
    """Return page showing all characters in the marvel cinematic universe"""


    characters = db.session.query(Character.character_id, Character.character_name, Character.civilian_name, Character.image1, Character.image2).all()

    return render_template("characters.html", 
                            characters=characters)

@app.route("/characters/<int:character_id>", methods=["GET"])
def show_character(character_id):
    """Return page showing the details of a selected movie.
    Show info about a movie.
    """

    char_info = Character.query.filter_by(character_id=character_id).one()
    char_movie = char_info.movies
    char_affil = char_info.affiliation

    
    return render_template("char_details.html",
                            char_info=char_info,
                            char_movie=char_movie,
                            char_affil=char_affil)

# @app.route("/affiliations")
# def list_affiliations():
#     """Return page showing all affiliations between characters in the marvel cinematic universe"""


#     affiliations = 

#     return render_template("characters.html", 
#                             characters=characters)

if __name__ == "__main__":
    app.debug = True

    connect_to_db(app)

    DebugToolbarExtension(app)

    app.run()