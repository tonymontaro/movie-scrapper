"""Application models."""

from app import db


class DBHelper(object):
    """Perform common SQLAlchemy tasks."""

    @staticmethod
    def add(item):
        """Add item to database."""
        db.session.add(item)
        db.session.commit()


class Movie(db.Model):
    """Movie model."""

    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    details = db.Column(db.Text())
    time = db.Column(db.String(255))
    duration = db.Column(db.String(255))

    @staticmethod
    def save(**kwargs):
        """Save a movie."""
        movie = Movie(**kwargs)
        DBHelper.add(movie)

    @staticmethod
    def get_all():
        """Get all movies."""
        return Movie.query.all()

    @staticmethod
    def get(id_):
        """Get a movie by ID."""
        movie = Movie.query.get(id_)
        if movie:
            return movie
        return None

    @staticmethod
    def find(query):
        """Find movies by search key."""
        movies = Movie.query.filter(Movie.name.contains(query)).all()
        return movies

    def get_content(self):
        """Return movie attributes and content as a dictionary."""
        movie = {
            'id': self.id,
            'name': self.name,
            'time': self.time,
            'details': self.details,
            'duration': self.duration
        }
        return movie
