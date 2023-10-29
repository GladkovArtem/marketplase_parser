import requests
from bs4 import BeautifulSoup


def parser_url(url):
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')

    list_urls = []
    for link in soup.find_all('a'):
        if 'https://www.wildberries.ru/catalog/' in link.get('href'):
            list_urls.append(link.get('href'))

    return list_urls
