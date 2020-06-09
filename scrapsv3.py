from bs4 import BeautifulSoup
import requests
from film import Film

films = Film()

for i in range(1, 501):
    print(f'Filmweb: {i}0/5000')
    source = requests.get(f'https://www.filmweb.pl/films/search?orderBy=count&descending=true&page={i}')
    source.raise_for_status()
    source = requests.get(f'https://www.filmweb.pl/films/search?orderBy=count&descending=true&page={i}').text
    soup = BeautifulSoup(source, 'lxml')

    for match in soup.find_all('div', class_='filmPreview__card'):
        try:
            netflix = match.find('div', class_='advertButton--netflix')
            if netflix:
                title = match.find('h2', class_='filmPreview__title').text
            #   title = title.rstrip()
                rate = match.find('span', class_='rateBox__rate').text
                films.fw_scores[title] = float(rate.replace(',', '.'))
        except:
            pass

films.sort_fw()
films.fw_save_to_txt('Najlepsze netflix z filmweb',
                     'Najlepsze netlfix/filmweb:')
