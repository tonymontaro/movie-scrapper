"""Movies API routes."""
from flask import Blueprint, jsonify, request

from app.models import Movie
from app.movies.helper import scrape_movies, get_earliest_movie_time

movies_bp = Blueprint('api', __name__)


@movies_bp.route('/', methods=['GET'], strict_slashes=False)
def home():
    """Get movies, refreshes every week.
    Movies can be filtered by with a query argument (q=search_term).
    Movies can also be sorted by name or time.
    Both sorting and filtering can be combined.
    """
    movies = Movie.get_all()
    if not movies:
        scrape_movies()
        movies = Movie.get_all()

    search = request.args.get('q')
    if search:
        movies = Movie.find(search)
    movies = [movie.get_content() for movie in movies]

    sort = request.args.get('sort')
    if sort and sort.lower() == 'name':
        movies = sorted(movies, key=lambda movie: movie['name'])
    elif sort and sort.lower() == 'time':
        movies = sorted(
            movies, key=lambda movie: get_earliest_movie_time(movie))

    return jsonify(movies), 200


@movies_bp.route('/<int:id_>', methods=['GET'])
def get_movie(id_):
    """Get a movie."""
    movie = Movie.get(id_)
    if movie:
        return jsonify(movie.get_content()), 200
    return jsonify({'message': 'Movie not found.'}), 404
