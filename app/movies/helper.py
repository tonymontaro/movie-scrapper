from urllib.request import urlopen
from bs4 import BeautifulSoup

from app.models import Movie


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

    for movie in movies:
        Movie.save(**movie)

    return movies
