import requests
import json

#main_url = 'https://api.jikan.moe/v3/anime/'
def create_url(anime_num):
    main_url = 'https://api.jikan.moe/v3/anime/'

    url_with_num = main_url + anime_num

    return url_with_num

def get_title(url):
    full_url = url + '/'

    response = requests.get(full_url)
    print(response.status_code)

    print(type(response.json()))
    data = response.json()
    print(data['title'])

def get_stats(url):
    full_url = url + '/stats'

    response = requests.get(full_url)
    print(response.status_code)

    print(type(response.json()))
    data = response.json()

    print('Completed: ', data['completed'])
    print('On hold: ', data['on_hold'])
    print('Plan to watch: ', data['plan_to_watch'])
    print('Dropped ', data['dropped'])