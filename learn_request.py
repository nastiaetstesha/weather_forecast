import requests
from urllib.parse import urlencode


def get_url():
    for city in cities:
        base_url = f'https://wttr.in/{requests.utils.quote(city)}'
        params = {
            'lang': 'ru',
            '3nTM': ''
        }
        response = requests.get(base_url, params=params)
        url = f'https://wttr.in/{requests.utils.quote(city)}&lang=ru?3nTM'
        response = requests.get(url)
        response.raise_for_status()
        print(response.text)

if __name__ == '__main__':
    cities = ['london', 'svo', 'череповец']
    get_url()