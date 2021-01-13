import matplotlib.pyplot as plt

labels = 'Completed', 'On_hold', 'Plan_to_watch', 'Dropped'

def create_plot(title, stats):
    
    fig1, ax1 = plt.subplots()
    ax1.pie(stats, labels=labels,autopct='%1.1f%%',shadow=False, startangle=90)
    ax1.axis('equal')
    plt.title(title, bbox={'facecolor':'0.8', 'pad':0})
    #plt.show()
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