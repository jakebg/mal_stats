

file = 'MAL_TOP_LIST.txt'
def get_anime_values():
    List = open(file).read().splitlines()
    #List = [ int(x) for x in List ]
    print(List)
    return List

