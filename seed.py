"""Utility file to seed ratings database from MovieLens data in seed_data/"""

from sqlalchemy import func
from model import connect_to_db, db, Character, Movie, Movie_Character, Group, CharacterGroup
from server import app
import requests


def load_movies():
    """Load movies from API via JSON into database."""
    
    print "Movies"

    payload = {"api_key":"d8ee42eb41cc997b74a9762e2a427de7"}

    #request to API for movie data, returns a JSON
    results = requests.get("http://api.themoviedb.org/3/keyword/180547/movies",params=payload)

    #turns JSON result into a dictionary
    json_dict = results.json()

    #provides my list
    movie_list = json_dict['results']

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

        if i % 100 ==0:
            print i

    db.session.commit()




# def set_val_user_id():
#     """Set value for the next user_id after seeding database"""

#     # Get the Max user_id in the database
#     result = db.session.query(func.max(User.user_id)).one()
#     max_id = int(result[0])

#     # Set the value for the next user_id to be max_id + 1
#     query = "SELECT setval('users_user_id_seq', :new_id)"
#     db.session.execute(query, {'new_id': max_id + 1})
#     db.session.commit()


if __name__ == "__main__":
    connect_to_db(app)

    # In case tables haven't been created, create them
    db.create_all()