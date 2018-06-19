[![Build Status](https://travis-ci.org/tonymontaro/movie-scrapper.svg?branch=master)](https://travis-ci.org/tonymontaro/movie-scrapper)
[![codecov](https://codecov.io/gh/tonymontaro/movie-scrapper/branch/master/graph/badge.svg)](https://codecov.io/gh/tonymontaro/movie-scrapper)
[![Maintainability](https://api.codeclimate.com/v1/badges/2353a8d56f839e175b4f/maintainability)](https://codeclimate.com/github/tonymontaro/movie-scrapper/maintainability)

# flask-starter-kit
A simple movies scrapper API that scraps and displays results from the [Silver Bird, Accra website.](https://silverbirdcinemas.com/cinema/accra/)


This repository contains just the API.

Hosted App: [Api hosted on Heroku.](https://d2-movie-scrapper.herokuapp.com/) 

Api documentation: [Generated with Postman](https://documenter.getpostman.com/view/646133/RWEgpdgi)



## Technologies Used
- [Python3.6](https://www.python.org/downloads/) - A programming language that lets you work more quickly.
- [Flask](flask.pocoo.org/) - A microframework for Python based on Werkzeug, Jinja 2 and good intentions.
- [Virtualenv](https://virtualenv.pypa.io/en/stable/) - A tool to create isolated virtual environments.
- [beautifulsoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - A tool for pulling data out of Html and XML files.

#### Extentsions

- [Flask-SQLAlchemy](http://flask-sqlalchemy.pocoo.org/2.3/) - For database management.
- [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/) - For migrations.
- [Flask-Login](https://flask-login.readthedocs.io/en/latest/) - For authentication.
- [Pytest](https://docs.pytest.org/en/latest/) - For testing.
- [APScheduler](https://apscheduler.readthedocs.io/en/latest/userguide.html) - For scheduling.


## Getting Started
Requirements
- Mac OS X, Windows or Linux
- Python 3.6

### Installation
- Clone this repository and cd into the root folder:

```bash
git clone https://github.com/tonymontaro/movie-scrapper.git && cd movie-scrapper
```

- Create and activate a virtual environment in python3:

```bash
virtualenv -p python3 venv && source venv/bin/activate
```

- Create a **.env** file and copy over content from the file **env_sample** on the root directory. In the **.env** file, you can specify things like the Database URL (the app uses sqlite by default but this behavior can be over-ridden here with something like postgres).
```bash
cp env_sample .env
```

- Install the dependencies:
```bash
pip install -r requirements.txt
```

- Migrations; run the following commands in order:
```bash
flask db init
flask db migrate
flask db upgrade
```
When a change is made to the `models`, the last two commands (migrate and upgrade) will need to be run.
- Finally, run the application
```bash
flask run
```

## Tests

- Run the tests with:
``` bash
pytest
```

#### Tests with coverage
- Show test coverage on the console: `pytest --cov=app`
- Generate html files containing test coverage: `pytest --cov=app --cov-report=html`


## License

MIT
