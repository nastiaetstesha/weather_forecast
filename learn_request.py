import requests


if __name__ == '__main__':
    cities = ['london', 'svo', 'череповец']

    for city in cities:
        url = f'https://wttr.in/{requests.utils.quote(city)}&lang=ru?3nTM'
        response = requests.get(url)
        response.raise_for_status()
        print(response.text)
