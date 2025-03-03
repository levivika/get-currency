from locale import currency

import requests
from bs4 import BeautifulSoup

url = 'https://www.alta.ru/currency/'

def get_html(url: str):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36'}
    response = requests.get(url, headers=headers)
    return response.text

def get_currency(html):
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('table', class_='js_sortable')
    rows = table.find_all('tr')
    pass

html = get_html(url)
currency=get_currency(html)
