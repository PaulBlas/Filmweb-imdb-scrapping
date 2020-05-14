from bs4 import BeautifulSoup
import requests
from film import Film

films = Film()

for i in range (1, 101):
    print(f'Filmweb: {i}0/1000')
    source = requests.get(f'https://www.filmweb.pl/films/search?orderBy=count&descending=true&page={i}')
    source.raise_for_status()
    source = requests.get(f'https://www.filmweb.pl/films/search?orderBy=count&descending=true&page={i}').text
    soup = BeautifulSoup(source, 'lxml')

    for match in soup.find_all('div', class_='filmPreview__card'):
        title = match.find('h2', class_='filmPreview__title').text
        # title = title.rstrip()
        rate = match.find('span', class_='rateBox__rate').text
        films.fw_scores[title] = float(rate.replace(',','.'))

for i in range(1, 1000, 50):
    print(f'Imdb: {i}/1000')
    source = requests.get(f'https://www.imdb.com/search/title/?groups=top_1000&start={i}&ref_=adv_nxt')
    source.raise_for_status()
    source = requests.get(f'https://www.imdb.com/search/title/?groups=top_1000&start={i}&ref_=adv_nxt').text
    soup = BeautifulSoup(source, 'lxml')

    for match in soup.find_all('div', class_='lister-item mode-advanced'):
        title = match.h3.a.text
        # title = title.rstrip()
        rate = match.strong.text
        films.imdb_scores[title] = float(rate.replace(',','.'))

films.merge()
films.sort()
films.fw_save_to_txt()
films.imdb_save_to_txt()
films.all_save_to_txt()
films.imdb_save_to_txt()



