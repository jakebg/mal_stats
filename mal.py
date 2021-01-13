from get_MAL import *

if __name__ == '__main__':
    url = create_url('40028')
    print(url)
    get_title(url)
    get_stats(url)