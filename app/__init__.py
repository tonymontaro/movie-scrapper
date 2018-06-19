"""Application entry point."""
import os

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

db = SQLAlchemy()
login_manager = LoginManager()

from config import app_config
from app.movies.routes import movies_bp
from app.movies.helper import scrape_movies, schedule_scrapping


def create_app(env):
    """Configure and create flask app."""
    app = Flask(__name__)
    app.secret_key = os.getenv('SECRET') or 'a-very-long-string'
    app.config.from_object(app_config[env])
    db.init_app(app)
    Migrate(app, db)
    login_manager.init_app(app)

    app.register_blueprint(movies_bp, url_prefix='/movies')

    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def catch_all(path):
        """Homepage and default page. Redirect non-existent urls here."""
        return jsonify({'message': 'Welcome to movie-scrapper API.'})

    @app.before_first_request
    def init_app():
        schedule_scrapping()

    return app


app = create_app(os.getenv('ENV', 'development'))
