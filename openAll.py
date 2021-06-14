# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 01:49:11 2021

@author: ASHUTOSH
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 11:13:19 2021

@author: ASHUTOSH
"""

#! python3
# searchpypi.py - Opens several search results.
import requests, sys, webbrowser, bs4
from webbrowser import Chrome

print('Searching...') # display text while downloading the search result page
res = requests.get('https://google.com/search?q='+ ' '.join(sys.argv[1:]))
res.raise_for_status()
# print(res.text)
f = open("googleSearch.htm", "w")
f.write(res.text)
f.close()
# Retrieve top search result links.
# Windows
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
soup = bs4.BeautifulSoup(res.text, 'html.parser')
# Open a browser tab for each result.
linkElems = soup.find_all('span')
f = open("spanResult.txt", "w")
f.write(str(linkElems))
f.close()
print(linkElems)
print(linkElems[0].find_all('span', {'class' : 'BNeawe'}))
chrome=webbrowser.Chrome()
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    if linkElems[i].find('a')['href']:
        urlToOpen = linkElems[i].find('a')['href']
        print('Opening', urlToOpen)
        webbrowser.open_new_tab('www.google.com'+urlToOpen)