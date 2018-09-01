"""Mock data and helper functions for testing."""
import json


def get_json(res):
    """Return json response as a dictionary or list."""
    return json.loads(res.data.decode('utf-8'))
