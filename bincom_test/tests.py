#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup


try:
    response = requests.get('https://techmeme.com/')
except requests.exceptions.ConnectionError:
    response = None

if response and response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    titles = soup.select(selector='div#topcol1 div.clus > .itc1 strong .ourh')
    summary = soup.select(selector='div#topcol1 div.clus > .itc1 div .ii')
    images = soup.select(selector='div#topcol1 div.clus > .itc1 .ill')
    links = []
    if titles:
        links = [i['href'] for i in titles]
        titles = [i.get_text().split('\n')[0] for i in titles]
    if summary:
        summary = [i.get_text() for i in summary]
    if images:
        images = [i['src'] for i in images]
    i = 0
    print(len(images), len(titles), len(summary))
    print(titles[0])
