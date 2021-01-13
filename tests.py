from get_MAL import *


def get_title_tests():

    url = 'https://api.jikan.moe/v3/anime/40028'
    test = get_title(url)
    if test == 'Shingeki no Kyojin: The Final Season':
        print('nice')
    else :
        print('not_nice')

    return
    # print(response.status_code)

    # print(type(response.json()))

def get_stats_tests():
    pass

if __name__ == '__main__':
    get_title_tests()
    
    # url = create_url('40028')
    # print(url)
    # get_title(url)
    # get_stats(url)