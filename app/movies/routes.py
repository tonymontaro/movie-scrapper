"""Movies API routes."""
from flask import Blueprint, jsonify, request

from app.models import Movie
from app.movies.helper import scrape_movies

movies_bp = Blueprint('api', __name__)


@movies_bp.route('/', methods=['GET'], strict_slashes=False)
def home():
    """Get movies for the week, refreshes every week."""
    movies = Movie.get_all()
    if not movies:
        movies = scrape_movies()
        [Movie.save(**movie) for movie in movies]
    else:
        movies = [movie.get_content() for movie in movies]

    return jsonify(movies), 200


@movies_bp.route('/<int:id_>', methods=['GET'])
def get_movie(id_):
    """Get a movie."""
    movie = Movie.get(id_)
    if movie:
        return jsonify(movie.get_content()), 200
    return jsonify({'message': 'Movie not found.'}), 404
