from flask import Blueprint, jsonify

from utils import *

database_blueprint = Blueprint('database_blueprint', __name__)


@database_blueprint.route('/movie/<title>')
def movie_page(title):
    movie = get_movie_by_title(title)
    return jsonify(movie)


@database_blueprint.route('/movie/<start_year>/to/<end_year>')
def movie_sor_by_year(start_year, end_year):
    movies = sort_movies_by_year(start_year, end_year)
    return jsonify(movies)


@database_blueprint.route('/movie/rating/<rating>')
def movies_sor_by_rating(rating):
    movies = sort_movies_by_rating(rating)
    return jsonify(movies)


@database_blueprint.route('/movie/genre/<genre>')
def movie_sor_by_rating(genre):
    movies = sort_movies_by_genre(genre)
    return jsonify(movies)
