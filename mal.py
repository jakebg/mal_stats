from get_MAL import *
from plot_MAL import *
from get_anime_values import *


import csv
import time
import pandas as pd
import numpy as np

def save_stats(title,stats):
    print(title)
    print(stats)
    pass

def create_mal_csv():
    with open('mal_stats.csv','w',newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["mal_id", "name", "watching", "completed","on_hold","dropped","plan_to_watch"])

    
def main(number):
    url = create_url(number)
    title,mal_id = get_title(url)
    stats = get_stats(url)
    joined_list = [mal_id,title,*stats]
    #print(title,mal_id,*stats)
    with open('mal_stats.csv', 'a') as f_object:
        writer_obj = csv.writer(f_object)
        writer_obj.writerow(joined_list)
        f_object.close()

    #save_stats(title,stats)
    # create_pie_plot(title, stats)
    # create_bar_plot()

if __name__ == '__main__':
    # create_mal_csv()
    # top_500 = get_anime_values()
    # top_3 = ['5114','38524','9253']
    # for x in top_3:
    #     main(x)
    #     time.sleep(4)

    df = pd.read_csv('mal_stats.csv')

    #print(df.mal_id,df.name)
    print(df.head)
    print('\n')
    sum_column = df["watching"]+df["completed"]+df["on_hold"]+df["dropped"]+df["plan_to_watch"]

    print(sum_column)
    print('\n')
    col_list = list(df)
    col_list.remove('mal_id')
    col_list.remove('name')
    #print(col_list)
    #print(df[col_list].iloc[:].sum(axis=1))
   # print(df[col_list])
    print(df[col_list].apply(lambda x: (x/x.sum())*100,axis=1))
    #print(res.reset_index())


    #create_bar_plot()
    #bar_chart_percent()
    #plt.show()
    # get_top_anime()
    pass