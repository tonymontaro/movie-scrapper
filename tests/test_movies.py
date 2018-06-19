"""Module for testing the user registration and login."""
import unittest

from app import create_app, db
from tests.helpers import get_json


class MovieTestCase(unittest.TestCase):
    """Movie tests."""

    def setUp(self):
        """Setup test client."""
        self.app = create_app("testing")
        self.client = self.app.test_client()
        with self.app.app_context():
            db.session.close()

    def test_get_movies(self):
        """Test getting all movies."""
        res = self.client.get('/movies')
        assert res.status_code == 200
        result = get_json(res)
        assert len(result) > 1
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
        assert result == sorted(result, key=lambda x: x['name'])


if __name__ == "__main__":
    unittest.main()
