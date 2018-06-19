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

    def test_get_a_movie(self):
        """Test getting a particular movie."""
        res = self.client.get('/movies/1')
        assert res.status_code == 200
        result = get_json(res)
        assert len(result) == 5

    def test_get_invalid_movie(self):
        """Test getting a non-existent movie"""
        res = self.client.get('/movies/3000000')
        assert res.status_code == 404
        result = get_json(res)
        assert result['message'] == 'Movie not found.'


if __name__ == "__main__":
    unittest.main()
