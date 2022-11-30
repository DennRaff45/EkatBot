import requests
import emoji
from bs4 import BeautifulSoup



res = requests.get('https://www.uralweb.ru/poster/cinema/')
soup = BeautifulSoup(res.text, 'html.parser')


film_name = soup.select('.poster-film-name')
genre = soup.select('.poster-film-gct')
href = soup.select('.poster-film-poster a')
age_rating = soup.select('.poster-film-name .age')
kp_rating = soup.select('.rt-kinopoisk')
imdb_rating = soup.select('.rt-imbd')


star = emoji.emojize(':star:')
camera = emoji.emojize(':cinema:')


out_cinema = []
def create_custom_out(film_name, genre, href, age_rating, kp_rating, imdb_rating):
    for i, item in enumerate(film_name):
        title = film_name[i].getText().strip().replace('\t', '').replace('\n', '')[:-3]
        age = age_rating[i].getText().strip().replace('\n', '').replace('\t', '')
        rating = kp_rating[i].getText().strip().replace('\n', '').replace('\t', '')
        imdb = imdb_rating[i].getText().strip().replace('\n', '').replace('\t', '')
        genre_and_duration = genre[i].getText().strip().replace('\n', '').replace('\t', '')
        hrefs = href[i].get('href', None)
        x = f'\n{camera}{title}, {age} \n{genre_and_duration}\n{star}Рейтинг КиноПоиск: {rating}\n{star}Рейтинг IMDB: {imdb}\nhttps://www.uralweb.ru{hrefs}\n'
        out_cinema.append(x)

create_custom_out(film_name, genre, href, age_rating, kp_rating, imdb_rating)

"""Return all films"""
string_out = ''.join(out_cinema)