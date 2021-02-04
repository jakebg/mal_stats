import matplotlib.pyplot as plt
import numpy as np
labels = 'Completed', 'On_hold', 'Plan_to_watch', 'Dropped'

def create_pie_plot(title, stats):
    
    fig1, ax1 = plt.subplots()
    ax1.pie(stats, labels=labels,autopct='%1.1f%%',shadow=False, startangle=90)
    ax1.axis('equal')
    plt.title(title, bbox={'facecolor':'0.8', 'pad':0})
    #plt.show()
    pass

def create_bar_plot():
    show = ['Fullmetal Alchemist: Brotherhood','Steins;Gate','Gintama°','Hunter x Hunter (2011)']
    completed = np.array([1561650,1126047,165050,1074063])
    on_hold = np.array([71651,60362,16411,77858])
    plan_to_watch = np.array([304479,420967,158730,237031])
    dropped = np.array([29953,35291,11350,31028])


    ind = [x for x, _ in enumerate(show)]

    plt.bar(ind, dropped, width=.8,label='dropped', color='orange')
    plt.bar(ind, plan_to_watch, width=.8, label='plan_to_watch', color='green', bottom = dropped)
    plt.bar(ind, on_hold, width =.8, label='on hold', color = 'yellow', bottom =  plan_to_watch + dropped)
    plt.bar(ind, completed, width =.8, label='completed', color='blue', bottom = on_hold + plan_to_watch + dropped )

    #plt.ylim([0,21])
    plt.xticks(ind,show)
    plt.ylabel("Status")
    plt.xlabel('Shows')
    plt.legend(loc="upper right")

    #plt.show()
    
# Completed:  33
# On hold:  3326
# Plan to watch:  150921
# Dropped  661

# labels = 'Completed', 'On_hold', 'Plan_to_watch', 'Dropped'
# sizes = [1561650, 71651, 304479, 29953]

# fig1, ax1 = plt.subplots()
# ax1.pie(sizes, labels=labels,autopct='%1.1f%%',shadow=True, startangle=90)
# ax1.axis('equal')

# plt.title('Fullmetal Alchemist: Brotherhood', bbox={'facecolor':'0.8', 'pad':0})
# plt.show()