# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 10:20:36 2021

@author: ASHUTOSH
"""

# First, you should install flickrapi
# pip install flickrapi

import flickrapi
import requests
import os

# Flickr api access key
flickr = flickrapi.FlickrAPI('c6a2c45591d4973ff525042472446ca2', '202ffe6f387ce29b', cache=True)

keyword = 'planets'

photos = flickr.walk(text=keyword,
                     tag_mode='all',
                     tags=keyword,
                     extras='url_c',
                     per_page=100,  # may be you can try different numbers..
                     sort='relevance')

urls = []
for i, photo in enumerate(photos):
    print(i)

    url = photo.get('url_c')
    urls.append(url)

    # get 50 urls
    if i > 5:
        break

print(urls)
os.makedirs('flickrF', exist_ok=True)
# Download image from the url and save it to '00001.jpg'
for url in urls:
    if url:
        res = requests.get(url)
        res.raise_for_status()
        # Save the image to ./xkcd.
        imageFile = open(os.path.join('flickrF', os.path.basename(url)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()