from get_MAL import *
from plot_MAL import *
# Fullmetal Alchemist: Brotherhood
# Shingeki no Kyojin: The Final Season
# Steins;Gate
# Gintama°
# Hunter x Hunter (2011)
anime_nums = ['5114', '40028', '9253', '28977', '11061']

def save_stats(title,stats):
    print(title)
    print(stats)
    pass

def main(number):
    url = create_url(number)
    title = get_title(url)
    stats,total = get_stats(url)
    save_stats(title,stats)
    # create_pie_plot(title, stats)
    # create_bar_plot()

if __name__ == '__main__':
    #for x in anime_nums:
    #    main(x)

        # main('5114')
        # main('9253')
    create_bar_plot()
    plt.show()

