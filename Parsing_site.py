import requests
from bs4 import BeautifulSoup


res = requests.get('https://www.uralweb.ru/poster/')
soup = BeautifulSoup(res.text, 'html.parser')
event_name = soup.select('.event-name')
date = soup.select('.event-time-and-place')
href = soup.select('.event-name a')
out = []
def create_custom_out(event_name, date, href):
    for i, item in enumerate(event_name):
        title = event_name[i].getText()
        place_and_date = date[i].getText().strip().replace('\t', '')
        hrefs = href[i].get('href', None)
        x = f'\n{title}, {place_and_date}\nhttps://www.uralweb.ru{hrefs}\n'
        out.append(x)

create_custom_out(event_name, date, href)

string_out = ''.join(out)

with open('События сегодня.txt', 'w', encoding='utf-8') as file:
    file.write(''.join(out))
