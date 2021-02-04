import requests
import json

#main_url = 'https://api.jikan.moe/v3/anime/'
def create_url(anime_num):
    main_url = 'https://api.jikan.moe/v3/anime/'

    url_with_num = main_url + anime_num

    return url_with_num

def get_title(url):
    full_url = url + '/'
    print(full_url)
    response = requests.get(full_url)
    data = response.json()

    print(data['title'])
    return data['title']

def get_stats(url):
    full_url = url + '/stats'

    response = requests.get(full_url)
    data = response.json()

    print('Completed: ', data['completed'])
    print('On hold: ', data['on_hold'])
    print('Plan to watch: ', data['plan_to_watch'])
    print('Dropped ', data['dropped'])

    total = data['completed'] + data['on_hold'] + data['plan_to_watch'] + data['dropped']
    
    print('\nTotal: ', total, '\n')

    stats = [data['completed'],data['on_hold'],data['plan_to_watch'],data['dropped']]
    return stats, total
