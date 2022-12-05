import requests
from bs4 import BeautifulSoup


res = requests.get('https://gorodzovet.ru/chel/')
soup = BeautifulSoup(res.text, 'html.parser')
event_name = soup.select('.event-block-title')
date = soup.select('.event-block-date')
href = soup.select('a.event-block-title')


out = []
def create_custom_out(event_name, href, date):
    for i, item in enumerate(event_name):
        title = event_name[i].getText().strip().replace('\n', '')
        dates = date[i].getText().strip().replace('\n', '')
        hrefs = href[i].get('href', None)
        x = f'\n{title}, {dates.replace(" ", "")}\nhttps://gorodzovet.ru{hrefs}\n'
        out.append(x)

create_custom_out(event_name, href, date)

"""Return all events"""
string_out = ''.join(out)
