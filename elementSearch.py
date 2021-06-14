# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 01:10:10 2021

@author: ASHUTOSH
"""

from selenium import webdriver
browser = webdriver.Firefox()
browser.get('https://inventwithpython.com')
try:
    elem = browser.find_element_by_tag_name('img')
    print('Found <%s> element with that src name!' % (elem.get_attribute('src')))
except:
    print('Was not able to find an element with that name.')