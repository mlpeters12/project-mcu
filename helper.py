from flask import Flask, render_template, redirect, request, flash, session, url_for
from jinja2 import StrictUndefined
import requests



def load_images(movie_id):
    """load multiple images per movie"""

    payload3 = {"api_key":"d8ee42eb41cc997b74a9762e2a427de7"}

    movie_id = str(movie_id)

    images = requests.get("http://api.themoviedb.org/3/movie/"+ movie_id +"/images",params=payload3)

    json_dict3 = images.json()

    image_list = json_dict3['backdrops']

    backdrop = []

    for image in image_list:
        backdrop.append(image['file_path'])

    return backdrop