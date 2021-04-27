import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')
labels = 'Completed', 'On_hold', 'Plan_to_watch', 'Dropped'

def create_pie_plot(title, stats):
    
    fig1, ax1 = plt.subplots()
    ax1.pie(stats, labels=labels,autopct='%1.1f%%',shadow=False, startangle=90)
    ax1.axis('equal')
    plt.title(title, bbox={'facecolor':'0.8', 'pad':0})
    #plt.show()
    pass

def create_bar_plot():

    # CHANGE TO PANDAS https://stackoverflow.com/questions/41296313/stacked-bar-chart-with-centered-labels
    show = ['Fullmetal Alchemist: Brotherhood','Steins;Gate','Gintama°','Hunter x Hunter (2011)']
    totals = [2031932, 1642667,351541,1419980]
    completed = np.array([1561650,1126047,165050,1074063])
    on_hold = np.array([71651,60362,16411,77858])
    plan_to_watch = np.array([304479,420967,158730,237031])
    dropped = np.array([29953,35291,11350,31028])

    ind = [x for x, _ in enumerate(show)]
    plt.bar(ind, completed, width =.8, label='completed', color='green' )
    plt.bar(ind, on_hold, width =.8, label='on hold', color = 'yellow', bottom =  completed )
    plt.bar(ind, plan_to_watch, width=.8, label='plan_to_watch', color='orange', bottom = on_hold + completed)
    plt.bar(ind, dropped, width=.8,label='dropped', color='red',bottom = on_hold + plan_to_watch + completed)

    #plt.ylim([0,21])
    plt.xticks(ind,show)
    plt.ylabel("Status")
    plt.xlabel('Shows')
    plt.legend(loc="upper right")

    #for 

    #plt.show()
def bar_chart_percent():
    show = ['Fullmetal Alchemist: Brotherhood','Steins;Gate','Gintama°','Hunter x Hunter (2011)']
    totals = [2031932,1642667,351541,1419980]
    completed = np.array([1610806,1126047,165050,1074063])
    on_hold = np.array([74097,60362,16411,77858])
    plan_to_watch = np.array([315716,420967,158730,237031])
    dropped = np.array([31313,35291,11350,31028])

    prop_complete = np.true_divide(completed,totals) * 100
    prop_hold     = np.true_divide(on_hold,totals) * 100
    prop_ptw      = np.true_divide(plan_to_watch,totals) * 100
    prop_drop     = np.true_divide(dropped,totals) * 100

    print(prop_complete)

    ind = [x for x, _ in enumerate(show)]

    plt.bar(ind, prop_complete, width =.8, label='completed', color='green' )
    plt.bar(ind, prop_hold, width =.8, label='on hold', color = 'yellow', bottom =  prop_complete )
    plt.bar(ind, prop_ptw, width=.8, label='plan_to_watch', color='orange', bottom = prop_hold + prop_complete)
    plt.bar(ind, prop_drop, width=.8,label='dropped', color='red',bottom = prop_hold +prop_ptw + prop_complete)

    plt.ylim=1.0
    plt.xticks(ind,show)
    plt.ylabel("Status")
    plt.xlabel('Shows')
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15),
          ncol=3, fancybox=True, shadow=True)
    pass
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