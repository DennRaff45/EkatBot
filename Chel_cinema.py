import requests
import emoji
from bs4 import BeautifulSoup



res = requests.get('https://chel.kinoafisha.info/movies/')
soup = BeautifulSoup(res.text, 'html.parser')


film_name = soup.select('.movieItem_title')
genre = soup.select('.movieItem_genres')
href = soup.select('a.movieItem_title')
country = soup.select('.movieItem_year')


camera = emoji.emojize(':cinema:')


out_cinema = []
def create_custom_out(film_name, genre, href, country):
    for i, item in enumerate(film_name):
        title = film_name[i].getText().strip().replace('\t', '').replace('\n', '')
        countries = country[i].getText().strip()
        genre_and_duration = genre[i].getText().strip().replace('\n', '').replace('\t', '')
        hrefs = href[i].get('href', None)
        x = f'\n{camera}{title}\n{genre_and_duration}\n{countries}\n{hrefs}\n'
        out_cinema.append(x)

create_custom_out(film_name, genre, href, country)

"""Return all films"""
string_out = ''.join(out_cinema)
