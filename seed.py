"""Utility file to seed ratings database from MovieLens data in seed_data/"""

from sqlalchemy import func
from model import connect_to_db, db, Character, Movie, MovieCharacter, Group, CharacterGroup
from server import app
import requests


def load_movies():
    """Load movies from API via JSON into database."""
    
    print "Movies"

    payload1 = {"page":"1","api_key":"d8ee42eb41cc997b74a9762e2a427de7"}
    payload2 = {"page":"2","api_key":"d8ee42eb41cc997b74a9762e2a427de7"}
    
    results1 = requests.get("http://api.themoviedb.org/3/keyword/180547/movies",params=payload1)
    results2 = requests.get("http://api.themoviedb.org/3/keyword/180547/movies",params=payload2)


    #turns JSON result into a dictionary
    json_dict1 = results1.json()
    json_dict2 = results2.json()


    #provides my list (concatenating list of dictionaries together)
    movie_list = json_dict1['results'] + json_dict2['results'] 

    for movie in movie_list:
        movie_id = movie['id']
        movie_name = movie['title']
        description = movie['overview']
        release_date = movie['release_date']
        image = movie['poster_path']

        new_movie_list = Movie(movie_id = movie_id,
                                movie_name = movie_name,
                                description = description,
                                release_date = release_date,
                                image = image)


        db.session.add(new_movie_list)

    db.session.commit()

# def load_characters():
#     """Load character info via a CSV file."""

#     print "Characters"

    


if __name__ == "__main__":
    connect_to_db(app)
    load_movies()
    # In case tables haven't been created, create them
    db.create_all()