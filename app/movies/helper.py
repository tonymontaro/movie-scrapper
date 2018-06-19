from urllib.request import urlopen
from bs4 import BeautifulSoup


def scrape_movies():
    """Scrape movies for the week from Silverbird/Accra cenema."""
    page = urlopen('https://silverbirdcinemas.com/cinema/accra/')
    soup = BeautifulSoup(page, 'html.parser')
    movies = soup.find_all('div', attrs={'class': 'entry-content'})[1:]
    movies = [
        {
            'duration': movie.find('div', attrs={'class': 'entry-date'}).text,
            'name': movie.find('h4', attrs={'class': 'entry-title'}).text,
            'time': movie.find(
                'p', attrs={'class': 'cinema_page_showtime'}).text,
            'details': movie.find('div', attrs={'class': 'desc-mv'}).text
        } for movie in movies
    ]
    return movies
