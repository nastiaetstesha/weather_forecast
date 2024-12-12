import requests
from urllib.parse import urlencode


cities = ['Лондон', 'Аэропорт шереметьево', 'Череповец']

def get_url():
    for city in cities:
        base_url = f'https://wttr.in/{city}'
        params = {
            'lang': 'ru',
            '3nTM': ''
        }
        query_string = urlencode(params)  
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        print(response.text)

if __name__ == '__main__':
    get_url()