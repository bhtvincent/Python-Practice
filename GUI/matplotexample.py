import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#plot 1 point by specifying its x and y coordinates

"""plt.plot(1,2,'mo')
1. plt.plot(3,1,'b+')
plt.plot(2,1,'xg')


plt.plot([1,2,3],[2,4,1],'-or')

plt.plot([2,4,1],'-gD')

2. x_values = np.arange(3,9,2)
y_values = x_values + 2

plt.plot(x_values,y_values,'--p')

songs_df = pd.read_csv('top2018.csv')
songs_df['rank']=songs_df.index+1
songs_df.set_index(('rank'),inplace = True)

songs_df['energy'].plot(c='m', marker = '.')
songs_df['danceability'].plot(c='g')

plt.xlabel('Song Rank')
plt.ylabel('Spotify Attributes')

plt.plot(songs_df['energy'],'b')
plt.plot(songs_df['danceability'],'r')

#plt.plot(songs_df['duration_ms'])

plt.legend()

ax = plt.gca()
ax.axis([1,99,0.2,1])
plt.tick_params(bottom = False, top = False,
                left = False, right = False,
                labelleft = False, labelbottom = False)

plt.title('Characteristics of Popular Songs')
plt.fill_between(range(1,100), songs_df['danceability'],songs_df['energy'],color = "yellow")

plt.show()"""

lang_pop = {'Python':27.35,'Java':20.64,'Javascript':8.4,'C#':7.45,'PHP':7.18,'C/C++':6.08}
#plt.bar(lang_pop.keys(),lang_pop.values(),color='cmgrby')
plt.pie(lang_pop.values(),explode = (0.1,0,0,0,0,0), labels = lang_pop.keys())
plt.show()