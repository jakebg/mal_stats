from get_MAL import *
from plot_MAL import *
# Fullmetal Alchemist: Brotherhood
# Shingeki no Kyojin: The Final Season
# Steins;Gate
# Gintama°
# Hunter x Hunter (2011)
anime_nums = ['5114', '40028', '9253', '28977', '11061']

def main(number):
    url = create_url(number)
    title = get_title(url)
    stats = get_stats(url)

    create_plot(title, stats)

if __name__ == '__main__':
    main('5114')
    main('9253')
    plt.show()

