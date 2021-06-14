# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 20:59:27 2021

@author: ASHUTOSH
"""

from bs4 import BeautifulSoup

import requests
import sys

url = 'http://www.imdb.com/chart/top'
response = requests.get(url)
# with open('imdb.txt','w') as im:
#     im.write(response.text)
soup = BeautifulSoup(response.text)
# soup.
tr = soup.findAll('tr')
# print(tr)
tr = iter(tr)
next(tr)

for movie in tr:
    title = movie.find('td', {'class': 'titleColumn'}).find('a').contents[0]
    year = movie.find('td', {'class': 'titleColumn'}).find('span', {'class': 'secondaryInfo'}).contents[0]
    rating = movie.find('td', {'class': 'ratingColumn imdbRating'}).find('strong').contents[0]
    row = title + ' - ' + year + ' ' + ' ' + rating
    print(row)