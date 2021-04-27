import requests
import json
import time

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

# Retrieves top anime numbers from myanimelist.com according to members
def get_top_anime():
    all_mal_IDS = []
    # full_url = 'https://api.jikan.moe/v3/top/anime/1/tv'
    # response = requests.get(full_url)
    # data = response.json()
    for i in range(10):
        full_url = f'https://api.jikan.moe/v3/top/anime/{i}/tv'
        response = requests.get(full_url)
        data = response.json()
        time.sleep(5)

        for x in range(50):
            #print(data['top'][x]['mal_id'])
            all_mal_IDS.append(data['top'][x]['mal_id'])

        with open('MAL_TOP_LIST.txt', 'w') as filehandle:
            for listitem in all_mal_IDS:
                filehandle.write('%s\n' % listitem)

    #return all_mal_IDS



