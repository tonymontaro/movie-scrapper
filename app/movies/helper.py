"""Movie helper module."""

import re
from urllib.request import urlopen
import atexit

from bs4 import BeautifulSoup
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger

from app.models import Movie, DBHelper


def scrape_movies():
    """Scrape movies for the week from Silverbird/Accra cenema."""
    page = urlopen('https://silverbirdcinemas.com/cinema/accra/')
    soup = BeautifulSoup(page, 'html.parser')
    movies = soup.find_all('div', attrs={'class': 'entry-content'})[1:]
    movies = [
        {
            'name': movie.find('h4', attrs={'class': 'entry-title'}).text,
            'duration': movie.find('div', attrs={'class': 'entry-date'}).text,

            'time': movie.find(
                'p', attrs={'class': 'cinema_page_showtime'}).text,
            'details': movie.find('div', attrs={'class': 'desc-mv'}).text
        } for movie in movies
    ]
    DBHelper.refresh_db()
    for movie in movies:
        Movie.save(**movie)

    return movies


def get_earliest_movie_time(movie_time):
    """Get the earliest date and time this week for a movie"""
    days = ['MON', 'TUE', 'WED', 'THUR', 'FRI', 'SAT', 'SUN']

    day = re.search(r'{}'.format('|'.join(days)), str(movie_time)).group()
    start = re.search(r'(\d+):(\d+)(AM|PM)', str(movie_time)).groups()
    return days.index(day), start[2], int(start[0]), int(start[1])


def schedule_scrapping():
    """Schedule scrapping the movies website every week"""
    scheduler = BackgroundScheduler()
    scheduler.start()
    scheduler.add_job(
        func=scrape_movies,
        trigger=IntervalTrigger(days=7),
        id='printing_job',
        name='Print date and time every five seconds',
        replace_existing=True)
    atexit.register(lambda: scheduler.shutdown())
