"""Module for testing the Movie-Scrapper API."""
import unittest

from app import create_app, db
from app.movies.helper import get_earliest_movie_time
from tests.helpers import get_json


class MovieTestCase(unittest.TestCase):
    """Movie Scrapper API tests."""
    app = None

    def setUp(self):
        """Setup test client."""
        self.app = MovieTestCase.app
        self.client = self.app.test_client()

    @classmethod
    def setUpClass(cls):
        cls.app = create_app("testing")
        with cls.app.app_context():
            db.session.close()
            db.drop_all()
            db.create_all()

    def test_get_movies(self):
        """Test getting all movies."""
        res = self.client.get('/movies')
        assert res.status_code == 200
        result = get_json(res)
        assert len(result) == 10
        self.movie1 = result[0]

    def get_first_movie(self):
        """Gets the first movie in database for testing."""
        return get_json(self.client.get('/movies'))[0]

    def test_get_a_movie(self):
        """Test getting a particular movie."""
        movie1 = self.get_first_movie()
        res = self.client.get('/movies/1')
        assert res.status_code == 200
        result = get_json(res)
        assert result == movie1

    def test_get_invalid_movie(self):
        """Test getting a non-existent movie"""
        res = self.client.get('/movies/3000000')
        assert res.status_code == 404
        result = get_json(res)
        assert result['message'] == 'Movie not found.'

    def test_search_movies_by_name(self):
        """Test searching for movies by name."""
        movie1 = self.get_first_movie()
        res = self.client.get('/movies?q={}'.format(movie1['name']))
        assert res.status_code == 200
        result = get_json(res)
        assert result[0] == movie1

    def test_sort_movies_by_name(self):
        """Test that movies can be sorted by name."""
        res = self.client.get('/movies?sort=name')
        assert res.status_code == 200
        result = get_json(res)
        assert result == sorted(result, key=lambda movie: movie['name'])

    def test_sort_movies_by_time(self):
        """Test that movies can be sorted by date."""
        res = self.client.get('/movies?sort=time')
        assert res.status_code == 200
        result = get_json(res)
        sorted_result = sorted(
            result, key=lambda movie: get_earliest_movie_time(movie))
        sorted_result_names = [x['name'] for x in sorted_result]
        assert [x['name'] for x in result] == sorted_result_names

    def test_homepage(self):
        """Test home route."""
        res = self.client.get('/')
        assert res.status_code == 200

    @classmethod
    def tearDownClass(cls):
        with cls.app.app_context():
            db.session.remove()
            db.drop_all()


if __name__ == "__main__":
    unittest.main()
